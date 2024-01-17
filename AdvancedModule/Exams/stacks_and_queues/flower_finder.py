from collections import deque

vowels = deque(input().split()) #queue
consonants = input().split() #stack

words = ['rose', 'tulip', 'lotus', 'daffodil']
find_letters = set()
find_word = ''

while vowels and consonants and not find_word:
    first_vowel = vowels.popleft()
    last_consonants = consonants.pop()

    for word in words:
        if first_vowel in word:
            find_letters.add(first_vowel)
        if last_consonants in word:
            find_letters.add(last_consonants)

        if find_letters.issuperset(word):
            find_word = word
            break

if find_word:
    print(f"Word found: {find_word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
