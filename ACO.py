import random
import GA
import settings as main_settings


# method_parameters = [ants, iterations, chromosome]


def ACO(iterations, ants, settings):
    '''
    ACO() takes 3 arguments:
    1. iterations - total number or runs
    2. ants - how many loops per run
    3. settings - user defined setting including number of variables,
        variable limits and variable types.

    Function compares generated chromosomes and the one with
    the lowest fitness is defined as "bestchromosome".
    A pheromone score is added to the  bestchromosome based on the number
    of ants it took to get it.

    Every iterations uses the pheromone score for a probability
    based choice of variable limits.
    '''
    bestchromosome = GA.random_chrom(
                                settings['nvariables'],
                                settings['variables_limits'])
    prob = random.randint(0, 100)
    for i in range(iterations):
        for j in range(ants):
            currentchromosome = GA.random_chrom(
                                    settings['nvariables'],
                                    settings['variables_limits'])
            if currentchromosome['fitness'] < bestchromosome['fitness']:
                bestchromosome = currentchromosome
                bestchromosome['pheromone'] += j//10
            if prob < bestchromosome['pheromone']:
                continue
            else:
                new_set = new_settings(bestchromosome, settings)
                bestEver = GA.random_chrom(
                                        settings['nvariables'],
                                        new_set['variables_limits'])
            if bestEver['fitness'] < bestchromosome['fitness']:
                bestchromosome = bestEver
    return bestchromosome


def new_settings(chromosome, settings):
    '''
    new_settings() takes 2 arguments:
    1. chromosome - bestchromosome from ACO based on pheromone probability
    2. settings - the original user defined settings.

    new_settings() is used to implement new variable limits
    based on the pheromone probability of ACO().
    It uses the bestchromosome values for each gene as the new
    lower limit for the next random chromosome.
    '''
    new_settings = {'variables_limits': list()}

    for i in range(settings['nvariables']):
        new_settings['variables_limits'].append(
            (chromosome['gene'][i],
                settings['variables_limits'][i][1],
                settings['variables_limits'][i][2]))

    return new_settings


def main():
    # settings variables (dict)
    settings = main_settings.heuristic_settings()

    best_population = list()
    # how many runs should the whole ACO program run
    runs = 1
    for i in range(runs):
        bestchromosome = ACO(100, 1000, settings)
        # add the best chromosome of each run to this list
        best_population.append(bestchromosome)
    best_population = GA.sort_population(best_population)

    print('Optimum Value = {}'.format(best_population[0]['fitness']))
    print('At values = {}'.format(best_population[0]['gene']))


if __name__ == '__main__':
    main()
