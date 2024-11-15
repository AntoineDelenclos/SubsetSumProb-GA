from src.ChromosomePopulationGenerator import ChromosomePopulationGeneration
from src.crossing import *
from src.fitnessFunction import evaluate
from src.mutation import *
from src.positions import positionBest, positionWorst
from src.strategies import *


#This return the final chromosome population after the first treatment and the fitness values associated, and also the set and the targeted value
def firstTreatment(pathFile, popNumber, popValueIs1Percent, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength, penalty):
    # Generation de la premiere population
    chromosomePop, A, Sa = ChromosomePopulationGeneration(pathFile, popNumber, popValueIs1Percent)

    # Mutations
    fitnessValue = evaluate(chromosomePop, A, Sa, penalty)
    bestPop = positionBest(fitnessValue, bestPopLength)
    chromosomePopMutation = mutation(chromosomePop, popNumber, percentPopMutated, lowPercentGenesMutated,
                                     highPercentGenesMutated, bestPop, A, Sa, penalty)

    # Croisement
    fitnessValue = evaluate(chromosomePopMutation, A, Sa, penalty)
    bestPop = positionBest(fitnessValue, bestPopLength)
    chromosomePopCrossing = crossing(popNumber, chromosomePopMutation, A, Sa, percentPopCrossing,
                                     lowPercentCutNumber, highPercentCutNumber, bestPop, penalty)

    chromosomePopFinal = betterOrNot(chromosomePop, chromosomePopCrossing, A, Sa, bestPop, penalty)
    fitnessValue = evaluate(chromosomePopFinal, A, Sa, penalty)

    return chromosomePopFinal, fitnessValue, A, Sa

#Permet d'effectuer l'algorithme génétique avec les opérations à effectuer dans l'ordre
def traitement(chromosomePop, A, Sa, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopulationCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength, newFullyRandomBestLength, worstPopLength, penalty):
    #Evaluation
    fitnessValue = evaluate(chromosomePop, A, Sa, penalty)
    bestPop = positionBest(fitnessValue, bestPopLength)
    worstPop = positionWorst(fitnessValue, worstPopLength)
    # Mutations
    chromosomePopMut = mutation(chromosomePop, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, bestPop, A, Sa, penalty)
    # Croisement
    chromosomePopCrossing = crossing(popNumber, chromosomePopMut, A, Sa, percentPopulationCrossing, lowPercentCutNumber, highPercentCutNumber, bestPop, penalty)

    chromosomePopPreFinal = betterOrNot(chromosomePop, chromosomePopCrossing, A, Sa, bestPop, penalty)

    chromosomePopFinal = strategyWorst(chromosomePopPreFinal, A, bestPop, worstPop, newFullyRandomBestLength, lowPercentGenesMutated, highPercentGenesMutated) #Replace worsts by new ones

    return chromosomePopFinal, fitnessValue

#Permet d'afficher la liste des solutions trouvées
def solutionList(chromosomePop, fitnessValue):
    # Finding all indexes of solutions with a fitness egal to 0
    listOfSolutionIndexes = [i for i, fitness in fitnessValue.items() if fitness == 0]
    listOfSolution = {}
    for i in range(len(listOfSolutionIndexes)):    #we find the chromosome corresponding to the solution
        solution = chromosomePop[i]
        if solution not in listOfSolution.values():
            listOfSolution.update({listOfSolutionIndexes[i]: solution})
    return listOfSolution
