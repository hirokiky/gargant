from gargant import make_gargant


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


def case_dispatcher(condition, route):
    return 'top'


def main(global_conf, root):
    condition = dict(db=dict(drum='ritsu',
                             bass='mio'))

    route = {'top': ('templates/index.mako', {'context1': (drummer_collector, element_builder1),
                                              'context2': (drummer_collector, element_builder2),
                                              'context3': (bassist_collector, element_builder3)})}

    return make_gargant(condition, route, case_dispatcher)
