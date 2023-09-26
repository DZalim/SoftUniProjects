budget = float(input())
price_for_kg_flour = float(input())

price_for_one_pack_of_eggs = 0.75 * price_for_kg_flour
price_for_one_litre_milk = 1.25 * price_for_kg_flour
price_for_loaf = (price_for_one_litre_milk/4) + price_for_kg_flour + price_for_one_pack_of_eggs

baked_loaves = 0
received_eggs = 0

while budget >= price_for_loaf:
    baked_loaves += 1
    received_eggs += 3
    if baked_loaves % 3 == 0:
        received_eggs -= baked_loaves - 2
    budget -= price_for_loaf

print(f"You made {baked_loaves} loaves of Easter bread! Now you have {received_eggs} eggs and {budget:.2f}BGN left.")
