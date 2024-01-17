n, m = input().split()

first_set = {int(input()) for _ in range(int(n))}
second_set = {int(input()) for _ in range(int(m))}

print(*first_set.intersection(second_set), sep = '\n')
