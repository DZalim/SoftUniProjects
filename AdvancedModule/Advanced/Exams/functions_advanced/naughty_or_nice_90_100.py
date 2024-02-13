def naughty_or_nice_list(list_of_kids, *args, **kwargs):

    kids_dict = {}

    for kid_value, kid_name in list_of_kids:
        kids_dict.setdefault(kid_value, [])
        kids_dict[kid_value].append(kid_name)

    dict_of_kids_types = {'Nice': [], 'Naughty': [], 'Not found': []}

    for value_type in args:
        value, type = value_type.split('-')
        value = int(value)

        if value in kids_dict:
            if len(kids_dict[value]) == 1:
                dict_of_kids_types[type].append(kids_dict[value][0])
                del kids_dict[value]

    for kid_name, kid_type in kwargs.items():
        for kid_point, kid_names in kids_dict.items():
            for name in kid_names:
                if kid_name == name:
                    dict_of_kids_types[kid_type].append(name)
                    kids_dict[kid_point].remove(kid_name)

    for kid_name in kids_dict.values():
        if kid_name:
            dict_of_kids_types['Not found'].append(kid_name[0])

    result = ''

    for type, names in dict_of_kids_types.items():
        if names:
            result += f"{type}: {', '.join(names)}\n"

    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
