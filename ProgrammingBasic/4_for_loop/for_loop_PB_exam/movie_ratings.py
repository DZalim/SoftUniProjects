number_of_film = int(input())

total_rate = 0

for film in range(number_of_film):
    name_of_film = input()
    film_rate = float(input())
    if film == 0:
        high_rate = film_rate
        high_film = name_of_film
        low_rate = film_rate
        low_film = name_of_film
        total_rate +=film_rate
    else:
        if film_rate > high_rate:
            high_rate = film_rate
            high_film = name_of_film
        if film_rate < low_rate:
            low_rate = film_rate
            low_film = name_of_film
        total_rate += film_rate

average_rate = total_rate / number_of_film

print(f"{high_film} is with highest rating: {high_rate:.1f}")
print(f"{low_film} is with lowest rating: {low_rate:.1f}")
print(f"Average rating: {average_rate:.1f}")
