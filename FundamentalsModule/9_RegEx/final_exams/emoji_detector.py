import re

text = input()

threshold_pattern = r"\d"
emoji_pattern = r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"

result_threshold_pattern = re.findall(threshold_pattern, text)
result_emoji_pattern = re.findall(emoji_pattern, text)

cool_threshold = 1
for number in result_threshold_pattern:
    cool_threshold *= int(number)
print(f"Cool threshold: {cool_threshold}")

print(f"{len(result_emoji_pattern)} emojis found in the text. The cool ones are:")
for emoji in result_emoji_pattern:
    emoji_coolnes = 0
    for char in emoji:
        emoji_coolnes += ord(char)
    if emoji_coolnes >= cool_threshold:
        print(emoji)
