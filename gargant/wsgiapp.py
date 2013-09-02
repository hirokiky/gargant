from paste.registry import RegistryManager, StackedObjectProxy

from webob.dec import wsgify
from webob.exc import HTTPNotFound

from gargant.context import context_builder, NotFound
from gargant.dispatch import dispatcher_factory, NotMetched
from gargant.respondent import respondent


condition = StackedObjectProxy()


def make_gargant(usercondition, route, root):
    @wsgify
    def _gargant(request):
        request.environ['paste.registry'].register(condition, usercondition)

        condition['request'] = request
        condition['route'] = route
        condition['root'] = root

        dispatcher = dispatcher_factory(root)

        try:
            case_name, matched = dispatcher(request.environ)
        except NotMetched:
            raise HTTPNotFound('condition did not matched any cases.')

        case = route[case_name]
        renderer_name, contexter = case[0]
        sideeffects = case[1:]

        try:
            context = context_builder(contexter, condition, *matched)
        except NotFound:
            raise HTTPNotFound

        response = respondent(renderer_name, context)

        for sideeffect, effection in sideeffects:
            effecter = context_builder(effection, condition, *matched)
            sideeffect(**effecter)

        return response
    return RegistryManager(_gargant)

