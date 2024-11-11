from ChromosomePopulationGenerator import ChromosomePopulationGeneration
from fitnessFunction import calculate_fitness, evaluate, betterOrNot
from src.crossing import crossing
from src.fitnessFunction import positionBest
from src.mutation import mutation
from src.traitement import traitement, solutionList


def main():
    path = "/home/quentin/PycharmProjects/SubsetSumProb-GA/data/xlarge/ssp_xlarge_1_pbm.txt"

    # Training Settings
    POPULATION_NUMBER = 30000
    PERCENT_POP_MUTATED = 0.4
    LOW_PERCENT_GENES_MUTATED = 0.1
    HIGH_PERCENT_GENES_MUTATED = 0.3
    PERCENT_POP_CROSSING = 0.8
    LOW_PERCENT_CUT_NUMBER = 0.02
    HIGH_PERCENT_CUT_NUMBER = 0.8
    BEST_POP_LENGTH = 10

    # Generation de la premiere population
    chromosomePop, A, Sa = ChromosomePopulationGeneration(path, POPULATION_NUMBER)

    #First treatment
    # Mutations
    fitnessValue = evaluate(chromosomePop, A, Sa)
    bestPop = positionBest(fitnessValue, BEST_POP_LENGTH)
    chromosomePopMutation = mutation(chromosomePop, POPULATION_NUMBER, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, bestPop)

    # Croisement
    fitnessValue = evaluate(chromosomePopMutation, A, Sa)
    bestPop = positionBest(fitnessValue, BEST_POP_LENGTH)
    chromosomePopCrossing = crossing(POPULATION_NUMBER, chromosomePopMutation, A, Sa, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, bestPop)

    chromosomeFinal = betterOrNot(chromosomePop, chromosomePopCrossing, A, Sa, bestPop)
    fitnessValue = evaluate(chromosomePopCrossing, A, Sa)

    # #Boucle jusqu'à temps que résolu
    while min(fitnessValue.values()) > 0:
        chromosomeFinal, fitnessValue = traitement(chromosomeFinal, A, Sa, POPULATION_NUMBER,PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH)


    listOfSolution = solutionList(chromosomeFinal, fitnessValue)
    print(listOfSolution)

    #Check fitnessValue : OK
    #print(fitnessValue[list(listOfSolution.keys())[0]])
    #print(fitnessValue[next(iter(listOfSolution))])




if __name__ == "__main__":
    main()
