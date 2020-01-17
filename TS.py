import random
from Fo import*
from GA import*
from settings import*




'''
TS function takes 2 arguments. The iterations (the number of runs), and settings (which is generated
by user input and includes number of variables, variable limits and variable type). 

TS() uses random_chrom() function from GA.py and compares the resulting fitness of each iteration 
to the one before it. If the current chromosome has a lower fitness, then this becomes the new
best chromosome.

The genes of every "bestchromosome" found is added to the tabu list. Every iterations checks 
the gene of the currenChromosome against the tabu list. If the gene is in the tabu list, the for
loop executes the "continue" command and adds 1 run to the iterations.
'''

def TS(iterations,settings):
	
	
	runs = iterations
	tabu = []
	bestchromosome = random_chrom(settings['nvariables'], settings['variables_limits'])
	
	for i in range(runs):
		currentChromosome = random_chrom(settings['nvariables'], settings['variables_limits'])
		if currentChromosome['gene'] in tabu:
			runs += 1
			continue
		if currentChromosome['fitness'] < bestchromosome['fitness']:
			bestchromosome = currentChromosome
			tabu.append(bestchromosome['gene'])
	
	print(bestchromosome, runs)


TS(1000, heuristic_settings())