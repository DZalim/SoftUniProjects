price_for_baggage_more_than_20_kg = float(input())
kg_baggage = float(input())
day_to_travel = int(input())
number_of_baggage = int(input())

price_for_baggage = 0

if kg_baggage > 20:
    price_for_baggage = price_for_baggage_more_than_20_kg * number_of_baggage
elif kg_baggage < 10:
    price_for_baggage = price_for_baggage_more_than_20_kg * 0.20 * number_of_baggage
else:
    price_for_baggage = price_for_baggage_more_than_20_kg * 0.50 * number_of_baggage

if day_to_travel > 30:
    price_for_baggage *= 1.1
elif day_to_travel < 7:
    price_for_baggage *= 1.4
else:
    price_for_baggage *= 1.15

print(f"The total price of bags is: {price_for_baggage:.2f} lv.")