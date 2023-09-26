price_for_baggage_more_than_20_kg = float(input())
kg_baggage = float(input())
day_to_travel = int(input())
number_of_baggage = int(input())

price_for_baggage_up_to_10_kg = price_for_baggage_more_than_20_kg * 0.20
price_for_baggage_between_10_and_20_kg = price_for_baggage_more_than_20_kg * 0.50

if day_to_travel > 30:
    price_for_baggage_more_than_20_kg *= 1.1
    price_for_baggage_between_10_and_20_kg *= 1.1
    price_for_baggage_up_to_10_kg *= 1.1
elif day_to_travel < 7:
    price_for_baggage_more_than_20_kg *= 1.4
    price_for_baggage_between_10_and_20_kg *= 1.4
    price_for_baggage_up_to_10_kg *= 1.4
else:
    price_for_baggage_more_than_20_kg *= 1.15
    price_for_baggage_between_10_and_20_kg *= 1.15
    price_for_baggage_up_to_10_kg *= 1.15

if kg_baggage > 20:
    price_for_baggage = price_for_baggage_more_than_20_kg * number_of_baggage
elif kg_baggage < 10:
    price_for_baggage = price_for_baggage_up_to_10_kg * number_of_baggage
else:
    price_for_baggage = price_for_baggage_between_10_and_20_kg * number_of_baggage

print(f"The total price of bags is: {price_for_baggage:.2f} lv.")


