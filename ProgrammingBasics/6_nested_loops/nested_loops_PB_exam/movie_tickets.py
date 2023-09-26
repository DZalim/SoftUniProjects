number_a1 = int(input())
number_a2 = int(input())
number_n = int(input())

for symbol_one in range(number_a1, number_a2):
    if symbol_one % 2 != 0:
        for symbol_two in range (1, number_n):
            for symbol_three in range(1, int(number_n/2)):
                if (symbol_one + symbol_two + symbol_three) % 2 != 0:
                    print(f"{chr(symbol_one)}-{symbol_two}{symbol_three}{symbol_one}")
