'''
This file biult for adding the Objective Function.
The main function is objective_funcion() to be called
from any other files such as GA and TS.
'''


def objective_function(chromosome):
    '''
    This function is the objective function for any case needed it only need
    a chromosome to return the fitness value.
    '''
    # Porosity example
    # Porosity function need 2 vaiables GSS and OSS with float range -1 to 1
    # Optimum value 1.04 @ GSS=1 and OSS=0
    # GSS = chromosome['gene'][0]
    # OSS = chromosome['gene'][1]
    # Porosity = 5.75 - 0.00009 * 40 - 0.00953 * 60 - 0.0195 * 20 + 0.208 * 1 \
    #     - 0.1313 * 90 - 0.327 * GSS - 0.456 * OSS - 0.000012 * (40 ** 2) \
    #     + 0.000017 * (60 ** 2) + 0.000106 * (20 ** 2) + 0.2283*(1 ** 2) \
    #     + 0.000946 * (90 ** 2) - 0.0934 * (GSS ** 2) + 0.1598 * (OSS ** 2) \
    #     + 0.000028 * 40 * 60 - 0.000068 * 40 * 20 + 0.00177 * 40 * 1 \
    #     + 0.000031 * 40 * 90 - 0.00003 * 40 * GSS + 0.00008 * 40 * OSS \
    #     + 0.000058 * 60 * 20 - 0.002092 * 60 * 1 - 0.000031 * 60 * 90 \
    #     + 0.00077 * 60 * GSS + 0.00072 * 60 * OSS - 0.00148 * 20 * 1 \
    #     + 0.000064 * 20 * 90 + 0.00179 * 20 * GSS + 0.00015 * 20 * OSS \
    #     + 0.00053 * 1 * 90 + 0.002 * 1 * GSS + 0.0191 * 1 * OSS \
    #     + 0.00136 * 90 * GSS + 0.00419 * 90 * OSS + 0.012 * GSS * OSS
    # chromosome['fitness'] = Porosity

    # Goldstein–Price function
    # Goldstein–Price function need 2 vaiables x and y with float range -2 to 2
    # Optimum value 3 @ x=0 and y=-1
    # x = chromosome['gene'][0]
    # y = chromosome['gene'][1]
    # Fxy = (1 + ((x + y + 1) ** 2) * (19 - 14 * x + 3 * (x ** 2) - 14 * y + 6 * x * y + 3 * (y ** 2))) \
    #         * (30 + ((2 * x - 3 * y) ** 2) * (18 - 32 * x + 12 * (x ** 2) + 48 * y - 36 * x * y + 27 * (y ** 2)))
    # chromosome['fitness'] = Fxy

    # Booth  function
    # Booth  function need 2 vaiables x and y with float range -10 to 10
    # Optimum value 0 @ x=1 and y=3
    x = chromosome['gene'][0]
    y = chromosome['gene'][1]
    Fxy = ((x + 2 * y - 7) ** 2) + ((2 * x + y - 5) ** 2)
    chromosome['fitness'] = Fxy

    return chromosome
