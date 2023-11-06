number_of_cars = int(input())

my_dict_with_car_information = {}

for car in range(number_of_cars):
    current_car, current_mileage, available_fuel = input().split("|")
    my_dict_with_car_information[current_car] = [int(current_mileage), int(available_fuel)]

command = input()
while command != "Stop":
    split_command = command.split(" : ")
    action = split_command[0]
    if action == "Drive":
        car_to_drive, given_distance, needed_fuel = split_command[1], int(split_command[2]), int(split_command[3])
        if my_dict_with_car_information[car_to_drive][1] < needed_fuel:
            print("Not enough fuel to make that ride")
        elif my_dict_with_car_information[car_to_drive][1] >= needed_fuel:
            my_dict_with_car_information[car_to_drive][0] += given_distance
            my_dict_with_car_information[car_to_drive][1] -= needed_fuel
            print(f"{car_to_drive} driven for {given_distance} kilometers. {needed_fuel} liters of fuel consumed.")
        if my_dict_with_car_information[car_to_drive][0] >= 100000:
            del my_dict_with_car_information[car_to_drive]
            print(f"Time to sell the {car_to_drive}!")
    elif action == "Refuel":
        car_to_refuel, quantity_to_fuel = split_command[1], int(split_command[2])
        if my_dict_with_car_information[car_to_refuel][1] + quantity_to_fuel > 75:
            quantity_to_fuel = 75 - my_dict_with_car_information[car_to_refuel][1]
        my_dict_with_car_information[car_to_refuel][1] += quantity_to_fuel
        print(f"{car_to_refuel} refueled with {quantity_to_fuel} liters")
    elif action == "Revert":
        car_to_revert, kilometers = split_command[1], int(split_command[2])
        my_dict_with_car_information[car_to_revert][0] -= kilometers
        if my_dict_with_car_information[car_to_revert][0] >= 10000:
            print(f"{car_to_revert} mileage decreased by {kilometers} kilometers")
        else:
            my_dict_with_car_information[car_to_revert][0] = 10000
    command = input()


for car_key, car_value in my_dict_with_car_information.items():
    print(f"{car_key} -> Mileage: {car_value[0]} kms, Fuel in the tank: {car_value[1]} lt.")
