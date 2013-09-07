class NotFound(Exception):
    pass


def context_builder(contexter, context):
    context = {name: builder(collector(context))
               for name, (collector, builder) in contexter.items()}
    return context
