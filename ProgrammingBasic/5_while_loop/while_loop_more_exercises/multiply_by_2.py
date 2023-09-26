
number = float(input())

while number >= 0:
    multiply = number * 2
    print(f"Result: {multiply:.2f}")
    number = float(input())

if number < 0:
    print("Negative number!")
