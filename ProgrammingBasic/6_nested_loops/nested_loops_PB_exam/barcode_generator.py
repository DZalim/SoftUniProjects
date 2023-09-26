start_range = input()
end_range = input()

for number_one in range(int(start_range[0]), int(end_range[0]) + 1):
    if number_one % 2 != 0:
        for number_two in range(int(start_range[1]), int(end_range[1]) + 1):
            if number_two % 2 != 0:
                for number_three in range(int(start_range[2]), int(end_range[2]) + 1):
                    if number_three % 2 != 0:
                        for number_four in range(int(start_range[3]), int(end_range[3]) + 1):
                            if number_four % 2 != 0:
                                print(f"{number_one}{number_two}{number_three}{number_four}", end=" ")
