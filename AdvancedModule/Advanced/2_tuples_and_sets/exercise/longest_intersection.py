longest_intersection = []

for _ in range(int(input())):
    first_side, second_side = input().split('-')
    first_start, first_end = first_side.split(',')
    second_start, second_end = second_side.split(',')
    left_side = set(int(x) for x in range(int(first_start), int(first_end)+1))
    right_side = set(int(x) for x in range(int(second_start), int(second_end)+1))

    intersection = [x for x in left_side.intersection(right_side)]
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
