h = float(input())
w = float(input())

weight_working_place = 0.70
lenght_working_place = 1.2
weight_hallway = 1
weight_chair = 1.60
lenght_chair = 1.20

weight_without_hallway = w - weight_hallway
working_place_weight = weight_without_hallway // weight_working_place
working_place_length =  h // lenght_working_place

total_working_place = working_place_length * working_place_weight - 3

print (total_working_place)
