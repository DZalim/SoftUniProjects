some_text = input().split()

filtered_text = [string for string in some_text if len(string) % 2 == 0]

print("\n".join(filtered_text))
