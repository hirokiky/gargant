from webob import Response

from mako.template import Template


def respondent(renderer_name, context):
    # TODO: Choosing renderer to return response as JSON and so on.
    renderer = renderer_factory(renderer_name)
    content = renderer(**context)
    response = Response(content)

    return response


def renderer_factory(renderer_name):
    template = Template(filename=renderer_name)
    return template.render

