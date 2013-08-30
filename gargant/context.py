def context_builder(contexter, condition):
    context = {name: builder(collector(condition))
               for name, (collector, builder) in contexter.items()}
    return context
