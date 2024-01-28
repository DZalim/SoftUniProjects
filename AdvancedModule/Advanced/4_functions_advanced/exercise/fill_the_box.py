def fill_the_box(height, length, width, *numbers):
    cub_size = height * length * width
    filled_cubs = 0

    index = 0
    while numbers[index] != 'Finish':
        filled_cubs += numbers[index]

        if cub_size <= filled_cubs:
            left_cubes = sum(cub for cub in numbers[index + 1:] if cub != 'Finish')
            return f"No more free space! You have {filled_cubs - cub_size + left_cubes} more cubes."

        index += 1

    return f"There is free space in the box. You could put {cub_size - filled_cubs} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
