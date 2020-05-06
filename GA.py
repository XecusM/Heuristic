'''
This file is for Genetic Algorithm modules it has
all functions needed for the Algorithm.
The list of functions:
    1. initial population
    2. cross over 'main function'
    3. survive population
    4. chromosome selection
    5. chromosome mutation
    6. intial chromosome
    7. sort population
    8. no deplication
    9. rank population
    10. stop time

NOTES:
Genatic Algorithm always want the minimum fitness value
so take care if you want the max. make the fitness negative values
'''
import Fo
import random
import datetime


def initial_population(chrm_size, pop_size, variables_limits):
    '''
    This function is returns a list of chromosomes as an initial_population.
    The function needs:
        1. The chromosome size (chrm_size)
        2. The population size (pop_size)
        3. The variables limits (variables_limits) of the paramters
            which contain [lower limit,upper limit,numbers type]
    '''
    # the output population
    out_pop = list()
    # create the population
    for i in range(pop_size):
        # chomosome data
        chromosome = {'gene': list(), 'fitness': float(), 'rank': int()}
        # create gene
        for j in range(chrm_size):
            if variables_limits[j][2] == 'integer':
                chromosome['gene'].append(random.randint(
                                                    variables_limits[j][0],
                                                    variables_limits[j][1]))
            elif variables_limits[j][2] == 'float':
                chromosome['gene'].append(random.uniform(
                                                    variables_limits[j][0],
                                                    variables_limits[j][1]))
            elif variables_limits[j][2] == 'boolean':
                chromosome['gene'].append(random.randint(
                                                    variables_limits[j][0],
                                                    variables_limits[j][1]))
        # get the chromosome fitness
        chromosome = Fo.objective_function(chromosome)
        # add chromosome to population
        out_pop.append(chromosome)
    # sort population
    out_pop = sort_population(out_pop)
    return out_pop


def random_chrom(chrm_size, variables_limits):
    '''
    This function is returns a random chromosome.
    The function needs:
        1. The chromosome size (chrm_size)
        2. The variables limits (variables_limits) of the paramters
            which contain [lower limit,upper limit,numbers type]
    '''
    # chomosome data
    chromosome = {'gene': list(), 'fitness': float(), 'rank': int()}
    # create gene
    for j in range(chrm_size):
        if variables_limits[j][2] == 'integer':
            chromosome['gene'].append(random.randint(
                                                    variables_limits[j][0],
                                                    variables_limits[j][1]))
        elif variables_limits[j][2] == 'float':
            chromosome['gene'].append(random.uniform(
                                                    variables_limits[j][0],
                                                    variables_limits[j][1]))
        elif variables_limits[j][2] == 'boolean':
            chromosome['gene'].append(random.randint(
                                                    variables_limits[j][0],
                                                    variables_limits[j][1]))
    # get the chromosome fitness
    chromosome = Fo.objective_function(chromosome)
    return chromosome


def sort_population(population, sort_key='fitness', max_on_top=False):
    '''
    This function needs unsorted population of chromosomes
    and returns a sorted one
    '''
    # sort population for 'fitness' key
    population = sorted(
                        population,
                        key=lambda k: k[sort_key],
                        reverse=max_on_top)
    return population


def chrom_selection(population, selection_method='fitness'):
    '''
    This function need the population as a list of chromosomes
    and returns a random chromosome
    '''
    # selection acording to method defined
    if selection_method == 'uniform':
        # select chromosome from population at uniform random
        chromosome = population[random.randint(0, len(population)-1)]
    elif selection_method == 'fitness':
        # rank population acording to its fitness
        population = rank_population(population)
        # random numbers limit for ranks
        lower_limit = 0
        upper_limit = population[0]['rank']
        # set counter for the chomosome after the selected one
        i = 1
        # select chromosome from population at fitness ranked random
        for chromosome in population:
            # create a random number
            random_number = random.randint(lower_limit, upper_limit)
            # check if the random number is fallen between
            # the chromosome rank and the next chromosome
            if population[i]['rank'] < random_number <= chromosome['rank']:
                break
            else:
                i += 1
                if i == len(population):
                    chromosome = population[-1]
                    break

    # test
    # print(chromosome)
    return chromosome


def survive_population(population, pop_size):
    '''
    This function for exclude the worse chromosomes from the population
    and return the population with its initial size
    '''
    # sort population
    population = sort_population(population)
    # remove the worse chromosomes
    while len(population) != pop_size:
        population.pop(-1)
    return population


def cross_over(population, variables_limits, method_parameters):
    '''
    This function create two new chromosomes from two random chromosomes
    selected from the given population.
    By cross-over one or more paramters according to given probability

    NOTE: the default value of probability is 0.5
    '''
    if method_parameters['cross_method'] == 'new_generation':
        # identify new population
        out_pop = list()
        while len(out_pop) < len(population):
            # get the two chromosomes
            chrom1 = chrom_selection(
                                    population,
                                    method_parameters['selection_method'])
            chrom2 = chrom_selection(
                                    population,
                                    method_parameters['selection_method'])
            # create the new two chromosomes
            for i in range(len(chrom1['gene'])):
                if random.random() <= method_parameters['cross_prob']:
                    x = chrom1['gene'][i]
                    chrom1['gene'][i] = chrom2['gene'][i]
                    chrom2['gene'][i] = x
            # mutate chrom1
            if random.random() <= method_parameters['mutation_prob']:
                chrom1 = mutation(
                                chrom1,
                                variables_limits,
                                method_parameters['mutation_prob'])
            # mutate chrom2
            if random.random() <= method_parameters['mutation_prob']:
                chrom2 = mutation(
                                chrom2,
                                variables_limits,
                                method_parameters['mutation_prob'])
            # calculate chromosomes fitness
            chrom1 = Fo.objective_function(chrom1)
            chrom2 = Fo.objective_function(chrom2)
            # check if the new chromosomes are not exist in the population
            if no_deplication(chrom1, out_pop):
                # add chromosome 1 to new population
                out_pop.append(chrom1)
            elif no_deplication(chrom1, out_pop):
                # add chromosome 2 to new population
                out_pop.append(chrom2)
            # sort new population
            out_pop = sort_population(out_pop)
        # remove excessive chromosomes
        out_pop = survive_population(out_pop, len(population))
        return out_pop
    elif method_parameters['cross_method'] == 'tournament':
        # get the population size
        pop_size = len(population)
        # get the two chromosomes
        chrom1 = chrom_selection(
                                population,
                                method_parameters['selection_method'])
        chrom2 = chrom_selection(
                                population,
                                method_parameters['selection_method'])
        # create the new two chromosomes
        for i in range(len(chrom1['gene'])):
            if random.random() <= method_parameters['cross_prob']:
                x = chrom1['gene'][i]
                chrom1['gene'][i] = chrom2['gene'][i]
                chrom2['gene'][i] = x
        # mutate chrom1
        if random.random() <= method_parameters['mutation_prob']:
            chrom1 = mutation(
                            chrom1,
                            variables_limits,
                            method_parameters['mutation_prob'])
        # mutate chrom2
        if random.random() <= method_parameters['mutation_prob']:
            chrom2 = mutation(
                            chrom2,
                            variables_limits,
                            method_parameters['mutation_prob'])
        # calculate chromosomes fitness
        chrom1 = Fo.objective_function(chrom1)
        chrom2 = Fo.objective_function(chrom2)
        # add the new chromosomes to the population
        population.append(chrom1)
        population.append(chrom2)
        # sort the population
        population = sort_population(population)
        # remove extra chromosomes from population
        population = survive_population(population, pop_size)
        return population
    else:
        return population


def mutation(chromosome, variables_limits, probability=0.5):
    '''
    This function mutate one or more paramters of the given
    chromosome according to given probability

    NOTE: the default value of probability is 0.5
    '''
    # mutate the chromosome paramters
    for i in range(len(chromosome['gene'])):
        if random.random() <= probability:
            if variables_limits[i][2] == 'integer':
                chromosome['gene'][i] = random.randint(
                                                    variables_limits[i][0],
                                                    variables_limits[i][1])
            elif variables_limits[i][2] == 'float':
                chromosome['gene'][i] = random.uniform(
                                                    variables_limits[i][0],
                                                    variables_limits[i][1])
            elif variables_limits[i][2] == 'boolean':
                chromosome['gene'][i] = random.randint(
                                                    variables_limits[i][0],
                                                    variables_limits[i][1])
        chromosome = Fo.objective_function(chromosome)
    return chromosome


def rank_population(population, rank_method='fitness'):
    '''
    This function for ranking the population to use this rank in selection
    '''
    # sort the population for the worse on top
    population = sort_population(population, 'fitness', True)
    # identify the intial values of the ranking
    rank_value = 1
    rank_step = 2
    # ranking the population
    for chromosome in population:
        chromosome['rank'] = rank_value
        rank_value += rank_step
        rank_step += 1
    # sort the population for the best on top
    population = sort_population(population, 'rank', True)
    return population


def no_deplication(chromosome, population):
    '''
    This function to check if the chromosome exist
    in the new population or not
    '''
    for chrom in population:
        if chrom['gene'] == chromosome['gene']:
            return False
            break
    return True


def stop_time(Stop_minutes=0, time_type='current'):
    '''
    This function to determine the stop time in minutes
    and return it or the current time
    '''
    if time_type == 'current':
        # get the current time in seconds
        now = datetime.datetime.now().day * 24 * 60 * 60 \
            + datetime.datetime.now().hour * 60 * 60 \
            + datetime.datetime.now().minute * 60 \
            + datetime.datetime.now().second
        # return the current time in seconds
        return now
    elif time_type == 'end':
        # get the crrent time
        now = datetime.datetime.now()
        # add the end time to our current time
        endtime = now + datetime.timedelta(minutes=Stop_minutes)
        # get end time in seconds
        endtime = endtime.day * 24 * 60 * 60 \
            + endtime.hour * 60 * 60 + endtime.minute * 60\
            + endtime.second
        # return the end time in seconds
        return endtime
    else:
        return 0
