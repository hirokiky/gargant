def context_builder(contexter, condition, **kwargs):
    context = {name: builder(collector(condition, **kwargs))
               for name, (collector, builder) in contexter.items()}
    return context
