def set_analyzer(sets_data, operation):
    converted_list = []

    for s in sets_data:
        sets = set(s)
        converted_list.append(sets)

    if operation == "intersection":
        result = converted_list[0]
        for s in converted_list[1:]:
            result &= s
        return sorted(list(result))

    elif operation == "union":
        result = converted_list[0]
        for s in converted_list[1:]:
            result |= s
        return sorted(list(result))

    elif operation == "difference":
        result = converted_list[0]
        for s in converted_list[1:]:
            result -= s
        return sorted(list(result))