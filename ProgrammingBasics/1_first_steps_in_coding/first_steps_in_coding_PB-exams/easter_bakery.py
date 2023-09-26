price_for_kg_of_flour = float(input())
kg_of_flour = float(input())
kg_of_sugar = float(input())
number_of_egg_shells = int(input())
packets_of_yeast = int(input())

price_for_kg_of_sugar = price_for_kg_of_flour * 0.75
price_for_egg_shell = price_for_kg_of_flour * 1.1
price_for_packet_of_yeast = price_for_kg_of_sugar * 0.20

expenses = price_for_kg_of_flour * kg_of_flour + kg_of_sugar * price_for_kg_of_sugar \
           + number_of_egg_shells * price_for_egg_shell + packets_of_yeast * price_for_packet_of_yeast

print(f"{expenses:.2f}")