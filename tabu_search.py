import random

# These are the global variables

# the total range of values that a given variable can take
valueRange = range(-100, 100)
# list of x and y values that give "bestFitness" by the tabu_search function
goodValues = []
# list of bes fitnesses obtained so far.
# This is used in both get_winners_First_round() and
# get_winners_Second_round() function. However it is cleared after
# the get_winners_First_round().
winners = []
# list of x and y values that have been used so far.
# This gets cleared whenever it reaches 50 values
# (in the tabu_search() function).
# This value can be changed to better optimise the search.
tabu = []


def set_xvalues(values):
    '''
    sets the x-value to a random number within a specified range.
    '''
    x = random.choice(values)
    return x


def set_yvalues(values):
    '''
    sets the x-value to a random number within a specified range.
    '''
    y = random.choice(values)
    return y


def objectiveFunction(x, y):
    '''
    the objective function. Will probably have to redo
    this function to fit with the GA.
    '''
    return ((x + 2 * y - 7) ** 2) + ((2 * x + y - 5) ** 2)


def tabu_search(valueRx, valueRy):
    '''
    the main tabu search function. For loop range
    and tabu list clearing can be tweaked as pleased.
    '''
    # starting value of bestFitness
    bestFitness = 999999

    for i in range(0, 3):
        x = set_xvalues(valueRx)
        y = set_yvalues(valueRy)

        # this nested if statement checks if the x and y values
        # are in the tabu list. if they are then it will skip to the
        # next iteration of the for-loop.
        if x in tabu:
            if y in tabu:
                continue

        # assigns objectiveFunction to fo variable
        fo = objectiveFunction(x, y)

        # adds x value to tabu list
        tabu.append(x)
        # adds y value to tabu list
        tabu.append(y)

        # checks if current fo value is lower than current bestFitness.
        if fo < bestFitness:
            bestFitness = fo
            # if fo is lower that bestFitness this will add
            # the x-value to the goodValues list
            goodValues.append(x)
            # if fo is lower that bestFitness this will add
            # the x-value to the goodValues list
            goodValues.append(y)

        # this clears the tabu list every time it reaches 50 values.
        # Can be changed as pleased.
        if 50 / len(tabu) == 1:
            tabu.clear()

    return bestFitness


def get_winners_First_round():
    '''
    this function goes through the tabu_search function 100 times
    and adds the bestFitness from each run to the winners list.
    '''
    for i in range(0, 100):
        winners.append(tabu_search(valueRange, valueRange))

    return winners


'''
This function (get_winner_Second_round) does:
    1) clears the tabu list and the winners list.
    2) sorts the goodValues list into sortedGoodValues
    3) uses the range of the sortedGoodValues in a new loop
        of tabu searches (currently set to 1000 loops)
    4) it adds the bestFitness of each iteration to the winners list.
    5) finally it sorts the list so the lowest fitness is the first item
'''


def get_winners_Second_round():
    tabu.clear()
    winners.clear()
    sorted_winners = []
    sortedGoodValues = sorted(goodValues)
    rangeOfGoodValues = range(sortedGoodValues[0], sortedGoodValues[-1])

    for k in range(0, 1000):
        winners.append(tabu_search(rangeOfGoodValues, rangeOfGoodValues))
        sorted_winners = sorted(winners)

    return sorted_winners


def main():
    get_winners_First_round()
    WIN = get_winners_Second_round()

    # prints the 100 lowest fitness values obtained.
    print(WIN[0:100])


if __name__ == '__main__':
    main()
