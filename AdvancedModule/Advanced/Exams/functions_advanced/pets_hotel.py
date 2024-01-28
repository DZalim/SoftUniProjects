def accommodate_new_pets(hotel_capacity, max_weight, *pets_info):
    total_pets = {}

    result = ''

    for pet_type, pet_weight in pets_info:
        if hotel_capacity == sum(total_pets.values()):
            result += f'You did not manage to accommodate all pets!\n'
            break

        if pet_weight <= max_weight:
            if pet_type not in total_pets:
                total_pets[pet_type] = 0
            total_pets[pet_type] += 1
    else:
        result += f"All pets are accommodated! Available capacity: {hotel_capacity - sum(total_pets.values())}.\n"

    result += f"Accommodated pets:\n"
    for pet, count in sorted(total_pets.items()):
        result += f"{pet}: {count}\n"

    return result.strip()


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
