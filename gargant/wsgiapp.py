from paste.registry import RegistryManager, StackedObjectProxy

from webob.dec import wsgify
from webob.exc import HTTPNotFound

from gargant.context import context_builder, NotFound
from gargant.dispatch import NotMatched
from gargant.respondent import respondent


condition = StackedObjectProxy()


def make_gargant(usercondition, route, tree):
    @wsgify
    def _gargant(request):
        request.environ['paste.registry'].register(condition, usercondition)

        condition['request'] = request
        condition['route'] = route
        condition['tree'] = tree

        try:
            node = tree(request.environ)
        except NotMatched:
            raise HTTPNotFound('condition did not matched any cases.')

        case = route[node.case]
        renderer_name, contexter = case[0]
        sideeffects = case[1:]

        tree_path = reversed(list(node))
        adapters = map(lambda x: x.adapter, tree_path)

        base_context = adapters[0](condition)
        for adapter in adapters[1:]:
            base_context = adapter(base_context)

        try:
            context = context_builder(contexter, base_context)
        except NotFound:
            raise HTTPNotFound

        response = respondent(renderer_name, context)

        for sideeffect, effection in sideeffects:
            effecter = context_builder(effection, base_context)
            sideeffect(**effecter)

        return response
    return RegistryManager(_gargant)
