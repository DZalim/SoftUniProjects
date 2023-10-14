population = [int(wealth) for wealth in input().split(", ")]
minimum_wealth = int(input())

possible_equal_distribution = True

for wealth_index in range(len(population)):
    if population[wealth_index] < minimum_wealth:
        needed_wealth_to_add = minimum_wealth - population[wealth_index]
        if max(population) - needed_wealth_to_add >= minimum_wealth:
            population[wealth_index] += needed_wealth_to_add
            population[population.index(max(population))] -= needed_wealth_to_add
        else:
            print("No equal distribution possible")
            possible_equal_distribution = False
            break

if possible_equal_distribution:
    print(population)
