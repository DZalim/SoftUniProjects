username = input()
user_password = input()

data_input = input()
while data_input != user_password:
    data_input = input()

print(f"Welcome {username}!")

