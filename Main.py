'''
This is the main program to control the Heuristic Techniques
and the objective function
'''
import GA
import PSO
import settings as main_settings


# get settings from settings file
settings = main_settings.heuristic_settings()
# get intial population
population = GA.initial_population(
                                settings['nvariables'],
                                settings['population_size'],
                                settings['variables_limits'])
# begin Calculating
print('Calculating...')
m = 0
# give the Calculations for every method selected
for method in settings['method']:
    # Genatic Algorithm
    if method == 'GA':
        if settings['stopping'][m][1] == 'minutes':
            i = 1
            # get the end time in minutes
            end_time = GA.stop_time(settings['stopping'][m][0], 'end')
            while end_time > GA.stop_time():
                # create a new population after cross over and mutation
                population = GA.cross_over(
                                        population,
                                        settings['variables_limits'],
                                        settings['method_parameters'][m])
                i += 1
        elif settings['stopping'][m][1] == 'iterations':
            for i in range(settings['stopping'][m][0]):
                # create a new population after cross over and mutation
                population = GA.cross_over(
                                        population,
                                        settings['variables_limits'],
                                        settings['method_parameters'][m])
            i += 1
        else:
            print('error in GA stopping criteria')
            quit()
        population = GA.sort_population(population)
        best_chromosome = population[0]
    elif method == 'TS':
        pass
    # Particle Swarm Algorithm
    elif method == 'PSO':
        # intiate the best_chromosome
        best_chromosome = GA.random_chrom(
                                        settings['nvariables'],
                                        settings['variables_limits'])
        # fill up the PSO_population for swarm Calculations
        PSO_population = {
                        'best_chromosome': best_chromosome,
                        'population': population
                    }
        if settings['stopping'][m][1] == 'minutes':
            i = 1
            # get the end time in minutes
            end_time = GA.stop_time(settings['stopping'][m][0], 'end')
            while end_time > GA.stop_time():
                # get the new population after swarming
                PSO_population = PSO.swarm(
                                        PSO_population,
                                        settings['variables_limits'],
                                        settings['method_parameters'][m])
                i += 1
        elif settings['stopping'][m][1] == 'iterations':
            for i in range(settings['stopping'][m][0]):
                # get the new population after swarming
                PSO_population = PSO.swarm(
                                        PSO_population,
                                        settings['variables_limits'],
                                        settings['method_parameters'][m])
            i += 1
        else:
            print('error in PSO stopping criteria')
            quit()
        # restore population after swarming
        population = PSO_population['population']
        # restore the best chromosome after swarming
        best_chromosome = PSO_population['best_chromosome']
        # remove velocity key from population
        for v in range(len(population)):
            # check if the velocity key exists in the popultion chromosome
            if 'velocity' in population[v].keys():
                # remove velocity key from the population chromosome
                del population[v]['velocity']
        # check if the velocity key exists in the best chromosome
        if 'velocity' in best_chromosome.keys():
            # remove velocity key from the best chromosome
            del best_chromosome['velocity']
    elif method == 'ACO':
        pass
    else:
        print('error in method selection')
        quit()
    m += 1

# Just for test
# print(population)
for chr in population:
    print(chr)
print(f"Number of iterations = {str(i)}")
# print(len(population))
print(best_chromosome)
# print(cross_chromosome)
# print(stop_time())
# print(end_time)
