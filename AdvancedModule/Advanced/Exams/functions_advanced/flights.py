def flights(*args):
    destinations = {}

    destination_index, passenger_index = 0, 1
    while args[destination_index] != 'Finish':
        current_dest, passengers = args[destination_index], args[passenger_index]
        if current_dest not in destinations:
            destinations[current_dest] = 0
        destinations[current_dest] += passengers

        destination_index += 2
        passenger_index += 2

    return destinations


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))