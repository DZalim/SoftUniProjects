price_of_mackerel = float(input())
price_of_sprinkle = float(input())
kg_of_bonito = float(input())
kg_of_safrid = float(input())
kg_of_calm = int(input())

price_of_bonito = price_of_mackerel + (price_of_mackerel * 0.60)
price_of_safrid = price_of_sprinkle + (price_of_sprinkle * 0.80)
proce_per_kg_of_calm = 7.50

total_for_bonito = kg_of_bonito * price_of_bonito
total_for_safrid = kg_of_safrid * price_of_safrid
total_for_calm = kg_of_calm * proce_per_kg_of_calm

total_price = total_for_bonito + total_for_safrid + total_for_calm

print(f'{total_price:.2f}')