def check_password(password):
    check_character = True
    check_letters_and_digits = True
    chek_digits = True
    if 6 > len(password) or len(password) > 10:
        check_character = False
        print("Password must be between 6 and 10 characters")
    digits = 0
    if not password.isalnum():
        check_letters_and_digits = False
        print("Password must consist only of letters and digits")
    for digit in password:
        if digit.isdigit():
            digits += 1
    if digits < 2:
        chek_digits = False
        print("Password must have at least 2 digits")
    if check_character == True and check_letters_and_digits == True and chek_digits == True:
        print("Password is valid")


password_for_check = input()
check_password(password_for_check)