from gargant.wsgiapp import make_gargant
from gargant.dispatch import Node, path_matching, method_matching


def drummer_collector(context):
    return context.ritsu


def bassist_collector(context):
    return context.mio


def element_builder1(drummer):
    return drummer + '!'


def element_builder2(drummer):
    return drummer + ' is kawaii'


def element_builder3(bassist):
    return bassist + ' is cool'


def sideeffect_factory(condition):
    def _sideeffect(**kwargs):
        print kwargs
    return _sideeffect


class HTTAdapter(object):
    def __init__(self, context):
        self.context = context

    @property
    def mio(self):
        return self.context['db']['drum']

    @property
    def ritsu(self):
        return self.context['db']['drum']


def main(global_conf, root):
    condition = {'db': {'drum': 'ritsu',
                        'bass': 'mio'}}

    tree = Node(
        (path_matching(['']),),
        children=(
            Node(
                (method_matching('get'),),
                case='top',
                name='top',
                adapter_factory=lambda x: lambda x: x,
            ),
            Node(
                (method_matching('post'),),
                case='countup',
                name='countup',
                adapter_factory=lambda x: lambda x: x,
            ),
        ),
        adapter_factory=lambda x: HTTAdapter
    )

    route = {
        'top': (
            ('templates/index.mako',
             {'context1': (drummer_collector, element_builder1),
              'context2': (drummer_collector, element_builder2),
              'context3': (bassist_collector, element_builder3)}),
        ),
        'countup': (
            ('templates/index.mako',
             {'context1': (drummer_collector, element_builder1),
              'context2': (drummer_collector, element_builder2),
              'context3': (bassist_collector, element_builder3)}),
            (sideeffect_factory(condition),
             {'context1': (drummer_collector, element_builder1)}),
        ),
    }

    return make_gargant(condition, route, tree)
