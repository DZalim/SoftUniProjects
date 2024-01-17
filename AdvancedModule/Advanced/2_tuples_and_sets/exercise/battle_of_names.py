odd_set = set()
even_set = set()

for index in range(1, int(input())+1):
    name = sum((ord(char) for char in input())) // index
    even_set.add(name) if name % 2 == 0 else odd_set.add(name)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep = ', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep= ', ')
