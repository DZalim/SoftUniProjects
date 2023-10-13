list_of_strings = input().split()
searched_palidnrome = input()

#palindromes = [word for word in list_of_strings if word == word[::-1]]

palindromes = [word for word in list_of_strings if word == "".join(reversed(word))]

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palidnrome)} times")
