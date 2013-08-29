def case_parser(case, condition):
    renderer_name, contexter = case
    context = {name: builder(collector(condition))
               for name, (collector, builder) in contexter.items()}
    # TODO: Providing to handle cases having side effects on.
    return renderer_name, context
