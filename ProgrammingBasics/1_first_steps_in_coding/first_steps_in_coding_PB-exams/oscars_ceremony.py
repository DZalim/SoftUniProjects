rent_for_the_hall = int(input())

statuettes = rent_for_the_hall * 0.70
catering = statuettes * 0.85
voicing = catering / 2

total = rent_for_the_hall + statuettes + catering + voicing

print(f"{total:.2f}")