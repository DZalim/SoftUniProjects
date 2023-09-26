number_a = int(input())
number_b = int(input())
max_generated_passwords = int(input())

password_counter = 0

for symbol_A in range(35, 56):
    for symbol_B in range(64, 97):
        for symbol_x in range(1, number_a +1):
            for symbol_y in range(1, number_b + 1):
                password_counter +=1
                print(f"{chr(symbol_A)}{chr(symbol_B)}{symbol_x}{symbol_y}{chr(symbol_B)}{chr(symbol_A)}", end= "|")
                symbol_A += 1
                if symbol_A > 55:
                    symbol_A = 35
                symbol_B += 1
                if symbol_B > 96:
                    symbol_B = 64
                if (password_counter == max_generated_passwords) or (symbol_x == number_a and symbol_y == number_b):
                    break
            if (password_counter == max_generated_passwords) or (symbol_x == number_a and symbol_y == number_b):
                break
        if (password_counter == max_generated_passwords) or (symbol_x == number_a and symbol_y == number_b):
            break
    if (password_counter == max_generated_passwords) or (symbol_x == number_a and symbol_y == number_b):
        break


