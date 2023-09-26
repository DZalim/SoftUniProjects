start_index = int(input())
last_index = int(input())

for current_index in range (start_index, last_index+1):
    print(f"{chr(current_index)}", end = " ")