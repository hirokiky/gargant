from webob.dec import wsgify
from webob.exc import HTTPNotFound

from gargant.case import case_parser
from gargant.dispatcher import dispatcher_fuctory, NotMetched
from gargant.respondent import respondent


def make_gargant(condition, route, root):
    @wsgify
    def _gargant(request):
        condition['request'] = request

        dispatcher = dispatcher_fuctory(root)

        try:
            case_name = dispatcher(condition)
        except NotMetched:
            raise HTTPNotFound('condition did not matched any cases.')

        renderer_name, context = case_parser(route[case_name], condition)

        response = respondent(renderer_name, context)

        return response
    return _gargant
