'''
import random
from Fo import *
from settings import *


#method_parameters = [ants, iterations, chromosome]

def random_chrom(chrm_size,variables_limits):
    
    This function is returns a random chromosome.
    The function needs:
        1. The chromosome size (chrm_size)
        2. The variables limits (variables_limits) of the paramters
            which contain [lower limit,upper limit,numbers type]
    
    #chomosome data
    chromosome={'gene':list(),'fitness':float(),'pheromone':int()}
    #create gene
    for j in range(chrm_size):
        if variables_limits[j][2]=='integer':
            chromosome['gene'].append(random.randint(variables_limits[j][0],variables_limits[j][1]))
        elif variables_limits[j][2]=='float':
            chromosome['gene'].append(random.uniform(variables_limits[j][0],variables_limits[j][1]))
        elif variables_limits[j][2]=='boolean':
            chromosome['gene'].append(random.randint(variables_limits[j][0],variables_limits[j][1]))
    #get the chromosome fitness
    chromosome=objective_function(chromosome)
    return chromosome



def ACO(iterations, ants):
  bestChromosome = {'gene':list(),'fitness':999,'pheromone':int()}
  prob = random.randint(0,100)


  for i in range(iterations):
  	for j in range(ants):
  		currentChromosome = random_chrom(settings['nvariables'], settings['variables_limits'])
  		

  		if currentChromosome['fitness'] < bestChromosome['fitness']:  			
  			bestChromosome = currentChromosome
  			bestChromosome['pheromone'] += j//10
  			if prob < bestChromosome['pheromone']:
  				continue
  			else:

	  			new_set = new_settings(bestChromosome)
	  			bestEver = random_chrom(settings['nvariables'], new_set['variables_limits'])
	  			if bestEver['fitness'] < bestChromosome['fitness']:
	  				bestChromosome = bestEver
	  
  			

  return bestChromosome

 


def new_settings(chromosome):
	

	new_settings = {
	'variables_limits' : []
	
	}


	for i in range(settings['nvariables']):
		new_settings['variables_limits'].append((chromosome['gene'][i],settings['variables_limits'][i][1], settings['variables_limits'][i][2]))


	return new_settings


settings = heuristic_settings() #global settings variable (dict)

def main():
	bestChromList = []
	epochs = 1 #how many runs should the whole ACO program run

	for i in range(epochs):
		
		
		f = ACO(100,1000)
		bestChromList.append(f['fitness']) #add the best fitness of each run to this list

	average = sum(bestChromList) / len(bestChromList) #average of each best fitness
	print(bestChromList, average)

if __name__ == '__main__':
	main()

'''

import random
from Fo import *
from settings import *


#method_parameters = [ants, iterations, chromosome]

def random_chrom(chrm_size,variables_limits):
    '''
    This function is returns a random chromosome.
    The function needs:
        1. The chromosome size (chrm_size)
        2. The variables limits (variables_limits) of the paramters
            which contain [lower limit,upper limit,numbers type]
    '''
    #chomosome data
    chromosome={'gene':list(),'fitness':float(),'pheromone':int()}
    #create gene
    for j in range(chrm_size):
        if variables_limits[j][2]=='integer':
            chromosome['gene'].append(random.randint(variables_limits[j][0],variables_limits[j][1]))
        elif variables_limits[j][2]=='float':
            chromosome['gene'].append(random.uniform(variables_limits[j][0],variables_limits[j][1]))
        elif variables_limits[j][2]=='boolean':
            chromosome['gene'].append(random.randint(variables_limits[j][0],variables_limits[j][1]))
    #get the chromosome fitness
    chromosome=objective_function(chromosome)
    return chromosome


'''
ACO() takes 3 arguments:
1. iterations - total number or runs
2. ants - how many loops per run
3. settings - user defined setting including number of variables, variable limits and variable types.

Function compares generated chromosomes and the one with the lowest fitness is defined as
"bestchromosome". A pheromone score is added to the  bestchromosome based on the number
of ants it took to get it.

Every iterations uses the pheromone score for a probability based choice of variable limits.
'''

def ACO(iterations,ants,settings):
    bestchromosome = random_chrom(settings['nvariables'], settings['variables_limits'])
    prob = random.randint(0,100)
    for i in range(iterations):
      for j in range(ants):
          currentchromosome = random_chrom(settings['nvariables'], settings['variables_limits'])
          if currentchromosome['fitness'] < bestchromosome['fitness']:
            bestchromosome = currentchromosome
            bestchromosome['pheromone'] += j//10
            if prob < bestchromosome['pheromone']:
              continue
            else:
              new_set = new_settings(bestchromosome,settings)
              bestEver = random_chrom(settings['nvariables'], new_set['variables_limits'])
              if bestEver['fitness'] < bestchromosome['fitness']:
                bestchromosome = bestEver
    return bestchromosome


'''
new_settings() takes 2 arguments:
1. chromosome - bestchromosome from ACO based on pheromone probability
2. settings - the original user defined settings.

new_settings() is used to implement new variable limits based on the pheromone
probability of ACO(). It uses the bestchromosome values for each gene as the new
lower limit for the next random chromosome.
'''

def new_settings(chromosome,settings):

  new_settings = {'variables_limits' : list()}

  for i in range(settings['nvariables']):
    new_settings['variables_limits'].append((chromosome['gene'][i],settings['variables_limits'][i][1], settings['variables_limits'][i][2]))


  return new_settings

def sort_population(population,sort_key='fitness',max_on_top=False):
    '''
    This function needs unsorted population of chromosomes and returns a sorted one
    '''
    #sort population for 'fitness' key
    population=sorted(population, key=lambda k: k[sort_key],reverse=max_on_top)
    return population


def main():
    #settings variables (dict)
    settings = heuristic_settings()

    best_population = list()
    #how many runs should the whole ACO program run
    runs = 1
    for i in range(runs):
        bestchromosome = ACO(100,1000,settings)
        #add the best chromosome of each run to this list
        best_population.append(bestchromosome)
    best_population=sort_population(best_population)
    
    print('Optimum Value = {}'.format(best_population[0]['fitness']))
    print('At values = {}'.format(best_population[0]['gene']))

if __name__ == '__main__':
    main()