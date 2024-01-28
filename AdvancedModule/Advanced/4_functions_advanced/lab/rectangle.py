def rectangle(*args):
    length = args[0]
    width = args[1]

    for number in args:
        if not isinstance(number, int):
            return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    return f'Rectangle area: {area()}\nRectangle perimeter: {perimeter()}'


print(rectangle(2, 10))
print(rectangle('2', 10))
