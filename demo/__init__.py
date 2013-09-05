from gargant.wsgiapp import make_gargant
from gargant.dispatch import Node, path_matching, method_matching


def drummer_collector(condition, *args):
    drummer = condition['db'].get('drum')
    return drummer


def bassist_collector(condition, *args):
    bassist = condition['db'].get('bass')
    return bassist


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


def main(global_conf, root):
    condition = {'db': {'drum': 'ritsu',
                        'bass': 'mio'}}

    tree = Node(
        (path_matching(['']),),
        children=(
            Node(
                (path_matching(['child']),),
                case='child',
                name='child',
                children=(
                    Node(
                        (path_matching(['granchild']),),
                        case='granchild',
                        name='granchild',
                    ),
                )
            ),
            Node(
                (method_matching('get'),),
                case='top',
                name='top',
            ),
            Node(
                (method_matching('post'),),
                case='countup',
                name='countup',
            ),
        )
    )

    route = {
        'top': (
            ('templates/index.mako',
             {'context1': (drummer_collector, element_builder1),
              'context2': (drummer_collector, element_builder2),
              'context3': (bassist_collector, element_builder3)}),
        ),
        'child': (
            ('templates/child.mako',
             {'context1': (drummer_collector, element_builder1)}),
        ),
        'granchild': (
            ('templates/child.mako',
             {'context1': (drummer_collector, element_builder2)}),
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
