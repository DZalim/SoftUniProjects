import random


def get_random_word(words):
    return random.choice(words)


names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "sees", "plays with", "brings"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

print("Hello, this is your first random sentence:")
while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}")
    question = input("Click [Enter] to generate new one.")
