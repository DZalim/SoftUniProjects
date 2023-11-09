usernames = input().split(", ")

for username in usernames:
    if 3 <= len(username) <= 16:
        for digit in username:
            if digit.isalnum() or digit == "-" or digit == "_":
                username_has_char = False
            else:
                username_has_char = True
                break
        if " " not in username and not username_has_char:
            print(username)
