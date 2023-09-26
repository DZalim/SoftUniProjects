stadium_capacity = int(input())
number_of_fans = int(input())

a = 0
b = 0
v = 0
g = 0

for fan in range(number_of_fans):
    sector = input()
    if sector == "A":
        a += 1
    elif sector == "B":
        b += 1
    elif sector == "V":
        v += 1
    elif sector == "G":
        g += 1

percent_a = a / number_of_fans * 100
percent_b = b / number_of_fans * 100
percent_v = v / number_of_fans * 100
percent_g = g / number_of_fans * 100
total_percent = number_of_fans / stadium_capacity * 100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{total_percent:.2f}%")


