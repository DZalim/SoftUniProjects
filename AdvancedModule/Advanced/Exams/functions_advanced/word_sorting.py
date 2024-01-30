def words_sorting(*words):
    words_sum = {}

    for word in words:
        ascii_sum = 0
        for char in word:
            ascii_sum += ord(char)
        words_sum[word] = ascii_sum

    sorted_words = sorted(words_sum.items(), key=lambda kvp: -kvp[1] if sum(words_sum.values()) % 2 != 0 else kvp[0])

    result = ''
    for key, value in sorted_words:
        result += f"{key} - {value}\n"

    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
