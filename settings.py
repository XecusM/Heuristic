'''
This file supply the main.py with settings for solving process
i.e. what method to use and how many itrations and sequance

in settings
method: GA,TS,PSO or ACO
Stopping: (#,'iterations') or (#,'minutes')
variables_limits: (#,#,'float') or (#,#,'integer') or (#,#,'boolean')
method_parameters:
    - GA {'cross_prob','mutation_prob','cross_method','selection_method'}
    - TS ()
    - PSO {'inertia_weight','cognative','social'}
    - ACO ()
'''
def heuristic_settings():
    #settings data
    settings = {
                'method':list(),'stopping':list(tuple()),'population_size':int(),'nvariables':int(),
                'variables_limits':list(tuple()),'method_parameters':list({})
                }
    #identify methods useds sequancially
    settings['method']=['PSO']
    #identify stopping criteria wheather time or iterations
    settings['stopping']=[(1,'minutes')]
    #set the population size useing during optimization
    settings['population_size']=15
    #number of variables on the objective function
    settings['nvariables']=2
    #the limit of every variable and its type
    settings['variables_limits']=[(-10,10,'float'),(-10,10,'float')]
    # setting method method_parameters
    settings['method_parameters']=[{'inertia_weight':0.5,'cognative':1,'social':1}]
    #return all settings to main.py
    return settings
