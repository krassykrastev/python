# A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what,
# and that is exactly what you are called to do for this problem.
# On the first line, you will be given the population (numbers separated by comma and space ", ").
# On the second line, you will be given the minimum wealth. You should distribute the wealth so that no part of the population
# has less than the minimum wealth. To do that, you should always take wealth from the wealthiest part of the population.
# There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible".
#
# Input1:
# 2, 3, 5, 15, 75
# 5
#
# Output1: [5, 5, 5, 15, 70]
#
# Input2:
# 2, 3, 5, 15, 75
# 20
#
# Output2: [20, 20, 20, 20, 20]
#
# Input3:
# 2, 3, 5, 45, 45
# 30
#
# Output3: No equal distribution possible

population_wealth = [int(s) for s in input().split(', ')]
minimum_wealth = int(input())

if minimum_wealth > sum(population_wealth) / len(population_wealth):
    print('No equal distribution possible')
    exit()

while any(x < minimum_wealth for x in population_wealth):
    max_number = max(population_wealth)
    number_to_change = min(population_wealth)
    index_max = population_wealth.index(max_number)
    index_min = population_wealth.index(number_to_change)
    added_value = minimum_wealth - number_to_change
    population_wealth[index_max] -= added_value
    population_wealth[index_min] += added_value

print(population_wealth)