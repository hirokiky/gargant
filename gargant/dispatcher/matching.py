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
