from webob.dec import wsgify
from webob.exc import HTTPNotFound

from gargant.context import context_builder
from gargant.dispatcher import dispatcher_factory, NotMetched
from gargant.respondent import respondent


def make_gargant(condition, route, root):
    @wsgify
    def _gargant(request):
        condition['request'] = request

        dispatcher = dispatcher_factory(root)

        try:
            case_name, matched = dispatcher(condition)
        except NotMetched:
            raise HTTPNotFound('condition did not matched any cases.')

        case = route[case_name]
        renderer_name, contexter = case[0]
        sideeffects = case[1:]
        context = context_builder(contexter, condition)

        response = respondent(renderer_name, context)

        for sideeffect, effection in sideeffects:
            effecter = context_builder(effection, condition)
            sideeffect(**effecter)

        return response
    return _gargant
