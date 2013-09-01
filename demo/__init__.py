from gargant import make_gargant
from gargant.dispatcher import node, path_matching, method_matching


def drummer_collector(condition):
    drummer = condition['db'].get('drum')
    return drummer


def bassist_collector(condition):
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

    root = (
        node('top',
             path_matching(['']), method_matching('GET')),
        node('countup',
             path_matching(['']), method_matching('POST'))
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

    return make_gargant(condition, route, root)
