class NotFound(Exception):
    pass


def context_builder(contexter, condition, *args):
    context = {name: builder(collector(condition, *args))
               for name, (collector, builder) in contexter.items()}
    return context
