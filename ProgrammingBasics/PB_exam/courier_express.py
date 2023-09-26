kg_of_packet = float(input())
type_of_service = input()
distance_in_km = int(input())

if kg_of_packet < 1:
    price_per_km = 0.03
    if type_of_service == "express":
        price_per_km += kg_of_packet * (0.80 * price_per_km)
elif 1 <= kg_of_packet < 10:
    price_per_km = 0.05
    if type_of_service == "express":
        price_per_km += kg_of_packet * (0.40 * price_per_km)
elif 10 <= kg_of_packet < 40:
    price_per_km = 0.10
    if type_of_service == "express":
        price_per_km += kg_of_packet * (0.05 * price_per_km)
elif 40 <= kg_of_packet < 90:
    price_per_km = 0.15
    if type_of_service == "express":
        price_per_km += kg_of_packet * (0.02 * price_per_km)
elif 90 <= kg_of_packet < 150:
    price_per_km = 0.20
    if type_of_service == "express":
        price_per_km += kg_of_packet * (0.01 * price_per_km)

total_price = price_per_km * distance_in_km

print(f"The delivery of your shipment with weight of {kg_of_packet:.3f} kg. would cost {total_price:.2f} lv.")
