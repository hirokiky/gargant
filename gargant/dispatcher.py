"""
root = (
    node(
        # leaf
        'top',
        matching(''),
        matching('')),
    ),
    node(
        # tree
        (
            node(# leaf
                 'child',
                 matching('')),
        ),
        matching(''),
    )
)
"""


class NotMetched(Exception):
    pass


true_matching = lambda x: lambda condition: True


def method_matching(method):
    def _matching(condition):
        return condition['request'].method == method
    return _matching


def path_mathching(path_list):
    def _matching(condition):
        return condition['request'].path.split('/')[1:] == path_list
    return _matching


def node(case_name, *matching):
    def _dispatch(condition):
        if all(map(lambda x: x(condition), matching)):
            return case_name
        else:
            return None
    return _dispatch


def dispatcher_fuctory(tree):
    def _dispatcher(condition):
        def handle_tree_or_leaf(tree_or_leaf):
            if isinstance(tree_or_leaf, str):
                return tree_or_leaf
            else:
                return _dispatcher(condition)
        for node in tree:
            tree_or_leaf = node(condition)
            if tree_or_leaf:
                return handle_tree_or_leaf(tree_or_leaf)
            else:
                continue
        else:
            raise NotMetched
    return _dispatcher
