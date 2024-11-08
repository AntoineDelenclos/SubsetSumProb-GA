from heapq import nsmallest, nlargest
import random

import numpy as np
import fitnessFunction

from ChromosomePopulationGenerator import ChromosomePopulationGeneration
from fitnessFunction import calculate_fitness

def main():
    path = "/home/antoine/PycharmProjects/SubsetSumProb-GA/data/small/ssp_small_1_pbm.txt"
    #Generation de la premiere population
    POPULATION_NUMBER = 1000
    chromosomePop, A, Sa = ChromosomePopulationGeneration(path, POPULATION_NUMBER)
    tenBest = []
    tenWorst = []
    fitnessValue = []
    fitnessPosition = {}
    for chromosome in chromosomePop:
        fitness = calculate_fitness(chromosome, A, Sa)
        fitnessValue.append(fitness)
        fitnessPosition[tuple(chromosome)] = fitness
        print(fitness)

    #10 best
    tenBest = nsmallest(10, fitnessValue)
    tenWorst = nlargest(10, fitnessValue)
    print(fitnessPosition)


    #Mutations
    populationMutationNumber = int(0.2 * POPULATION_NUMBER) #Mutation sur 20% de la population
    countMutations = 0
    for chromosome in chromosomePop:
        print(chromosome)
        while countMutations < populationMutationNumber:
            positionPop = random.randint(0, POPULATION_NUMBER - 1)

            geneNumberTransformed = random.randint(int(0.1) * len(chromosome), int(0.4) * len(chromosome)) #Entre 10% et 40% de gènes mutés

            specificTransformedGenes = [random.randint(0, len(chromosome)) for i in range(geneNumberTransformed)] #On sélectionne les gènes du chromosome qui vont muter

            for k in range(len(specificTransformedGenes)): #On va switch la valeur du gène muté entre 0 et 1
                chromosomePop[positionPop][specificTransformedGenes[k]] = (chromosomePop[positionPop][specificTransformedGenes[k]] + 1)%2

            countMutations += 1
        print(chromosome)


    #Croisement
    for chromosome in chromosomePop:

    # #Boucle jusqu'à temps que résolu
    # while (1 == 1):
    #
    #
    #     #Scoring
    #    #for chromosome in chromosomePop:
    #      #  calculate_fitness(chromosome, A, Sa)

if __name__ == "__main__":
    main()