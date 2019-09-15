from Fo import *
from GA import *
import random
'''
This file is for Particle Swarm modules it has all functions needed for the Algorithm.
The list of functions:
    1. swarm
    2. intial velocity
    2. update velocity
    3. update position

NOTES:
Particle Swarm always want the minimum fitness value so take care if you want the max. make the fitness negative values
'''
def swarm(PSO_population,variables_limits,method_parameters):
    '''
    This the main function for Particle Swarm Algorithm it needs
        1. dictionary of population list and best_chromosome dictionary (PSO_population)
        2. a list of tuples each tuple has the minimum, maximum and varible type (variables_limits)
        3. dictionary of (method_parameters) contain inertia weight, cognative and social constants
    And returns the new (PSO_population)
    '''
    # extract population from PSO_population
    population=PSO_population['population']
    # extract best_chromosome from PSO_population
    best_chromosome=PSO_population['best_chromosome']
    # add velocity for the initial population and best_chromosome
    if not 'velocity' in population[0]:
        # get the initial velocities for each Particle
        population=intial_velocity(population,variables_limits)
        # sort population by fitness to get the best chromosome
        population=sort_population(population)
        # get the best chromosome from the sorted population
        best_chromosome=population[0]
        # update postions for population by adding the velocity
        population=update_position(population,variables_limits)
        # sort population by fitness to get the best chromosome
        population=sort_population(population)
        # check if the best_chromosome better than the population best chromosome
        if population[0]['fitness']<best_chromosome['fitness']:
            best_chromosome=population[0]
        # restore populatio to PSO_population
        PSO_population['population']=population
        # restore best_chromosome to PSO_population
        PSO_population['best_chromosome']=best_chromosome
    else:
        # get the new velocities for each Particle
        population=update_velocity(population,best_chromosome,method_parameters,variables_limits)
        # sort population by fitness to get the best chromosome
        population=sort_population(population)
        # get the best chromosome from the sorted population
        best_chromosome=population[0]
        # update postions for population by adding the velocity
        population=update_position(population,variables_limits)
        # sort population by fitness to get the best chromosome
        population=sort_population(population)
        # check if the best_chromosome better than the population best chromosome
        if population[0]['fitness']<best_chromosome['fitness']:
            best_chromosome=population[0]
        # restore populatio to PSO_population
        PSO_population['population']=population
        # restore best_chromosome to PSO_population
        PSO_population['best_chromosome']=best_chromosome
    return PSO_population

def intial_velocity(population,variables_limits):
    '''
    This function is to add the key of velocity for the population with its initial values
    it needs the population and variables_limits to return population have the initial velocities
    '''
    for i in range(0,len(population)):
        # add velocity key to population chromosomes
        population[i]['velocity']=list()
        # add initial velocities
        for j in range(0,len(population[i]['gene'])):
            # check if the variables wheather float of integer
            if variables_limits[j][2]=='float':
                population[i]['velocity'].append(random.uniform(-1,1))
            else:
                population[i]['velocity'].append(random.randint(-1,1))
    return population

def update_velocity(population,best_chromosome,method_parameters,variables_limits):
    '''
    This function calculates the new velocities for every Particle
    it needs the population, the best chromosome, method parameters and variables limits
    And returns the population with its updated velocities
    '''
    # get inertia weight constant
    w=method_parameters['inertia_weight']
    # get the cognative constant
    c1=method_parameters['cognative']
    # get the social constant
    c2=method_parameters['social']
    # sort the population to its best chromosome
    population=sort_population(population)
    for i in range(0,len(population)):
        for j in range(0,len(population[i]['gene'])):
            # identify r1
            r1=random.random()
            # identify r2
            r2=random.random()
            # calculate velocity of cognative
            velocity_cognative=c1*r1*(population[0]['gene'][j]-population[i]['gene'][j])
            # calculate velocity of social
            velocity_social=c2*r2*(best_chromosome['gene'][j]-population[i]['gene'][j])
            # check if the variables wheather float of integer
            if variables_limits[j][2]=='float':
                population[i]['velocity'][j]=w*population[i]['velocity'][j]+velocity_cognative+velocity_social
            else:
                population[i]['velocity'][j]=int(w*population[i]['velocity'][j]+velocity_cognative+velocity_social)
    return population

def update_position(population,variables_limits):
    '''
    This function gives the new positions for every particle by getting the population and variables limits
    It returns the populaiton with the new positions
    '''
    for i in range(0,len(population)):
        for j in range(0,len(population[i]['gene'])):
            # calculate the new position
            population[i]['gene'][j]=population[i]['gene'][j]+population[i]['velocity'][j]
            # check if the new position exceed the upper varible limit
            if population[i]['gene'][j]>variables_limits[j][1]:
                population[i]['gene'][j]=variables_limits[j][1]
            # check if the new position below the lower varible limit
            if population[i]['gene'][j]<variables_limits[j][0]:
                population[i]['gene'][j]=variables_limits[j][0]
        # get the fitness for the new position
        population[i]=objective_function(population[i])
    return population
