n = int(input())

sum_right = 0
sum_left = 0

for num in range(n):
    num_right = int(input())
    sum_right += num_right

for num in range(n):
    num_left = int(input())
    sum_left += num_left

if sum_right == sum_left:
    print(f"Yes, sum = {sum_right}")
else:
    diff = abs(sum_right - sum_left)
    print(f"No, diff = {diff}")
