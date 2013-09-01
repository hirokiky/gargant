class NotMetched(Exception):
    pass


true_matching = lambda x: lambda condition: True


def method_matching(method):
    def _matching(condition):
        return condition['request'].method == method
    return _matching


def brace_match(s):
    if s.startswith('{') and s.endswith('}'):
        return s.strip('{}')


def path_matching(matching_list):
    def _matching(condition):
        url_kwargs = {'matching_list': matching_list}
        path_list = condition['request'].path.split('/')[1:]
        for path, matching in map(None, path_list, matching_list):
            key = brace_match(matching)
            if key:
                url_kwargs[key] = path
                continue
            else:
                if path != matching:
                    return None
                else:
                    continue
        else:
            return url_kwargs
    return _matching
