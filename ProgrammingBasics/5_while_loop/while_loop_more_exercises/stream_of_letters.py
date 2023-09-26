word = ""
words = ""

c_counter = 0
o_counter = 0
n_counter = 0

command = input()
while command != "End":
    if chr(65) <= command <= chr(90) or chr(97) <= command <= chr(122):
        if command != "c" and command != "o" and command != "n":
            word += command
        else:
            if command == "c":
                c_counter += 1
                if c_counter > 1:
                    word += command
            elif command == "o":
                o_counter += 1
                if o_counter > 1:
                    word += command
            elif command == "n":
                n_counter += 1
                if n_counter > 1:
                    word += command
        if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
            word += " "
            words += word
            word = ""
            c_counter = 0
            o_counter = 0
            n_counter = 0
    command = input()

print(words)



