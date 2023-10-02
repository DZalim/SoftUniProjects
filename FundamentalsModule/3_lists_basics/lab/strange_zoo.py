# tail = input()
# body = input()
# head = input()
#
# current_list = [head, body, tail]
#
# print(current_list)

tail = input()
body = input()
head = input()

current_list = [tail, body, head]
current_list[0], current_list[2] = current_list[2], current_list[0]
print(current_list)