from webob.dec import wsgify

from gargant.case import case_parser
from gargant.respondent import respondent


def make_gargant(condition, route, case_dispatcher):
    @wsgify
    def _gargant(request):
        condition['request'] = request

        case_name = case_dispatcher(condition, route)

        renderer_name, context = case_parser(route[case_name], condition)

        response = respondent(renderer_name, context)

        return response
    return _gargant
