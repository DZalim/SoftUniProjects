def start_spring(**type_of_spring):
    spring_dict = {}

    for spring_object, spring_type in type_of_spring.items():
        if spring_type not in spring_dict:
            spring_dict[spring_type] = []
        spring_dict[spring_type].append(spring_object)

    sorted_dict = sorted(spring_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''

    for spring_type, spring_objects in sorted_dict:
        result += f'{spring_type}:\n'
        for spring_object in sorted(spring_objects):
            result += f'-{spring_object}\n'

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
