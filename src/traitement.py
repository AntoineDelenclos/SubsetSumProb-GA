from src.ChromosomePopulationGenerator import ChromosomePopulationGeneration
from src.crossing import crossing
from src.fitnessFunction import evaluate, positionBest, betterOrNot
from src.mutation import mutation


#This return the final chromosome population after the first treatment and the fitness values associated, and also the set and the targeted value
def firstTreatment(pathFile, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength):
    # Generation de la premiere population
    chromosomePop, A, Sa = ChromosomePopulationGeneration(pathFile, popNumber)

    # Mutations
    fitnessValue = evaluate(chromosomePop, A, Sa)
    bestPop = positionBest(fitnessValue, bestPopLength)
    chromosomePopMutation = mutation(chromosomePop, popNumber, percentPopMutated, lowPercentGenesMutated,
                                     highPercentGenesMutated, bestPop, A, Sa)

    # Croisement
    fitnessValue = evaluate(chromosomePopMutation, A, Sa)
    bestPop = positionBest(fitnessValue, bestPopLength)
    chromosomePopCrossing = crossing(popNumber, chromosomePopMutation, A, Sa, percentPopCrossing,
                                     lowPercentCutNumber, highPercentCutNumber, bestPop)

    chromosomeFinal = betterOrNot(chromosomePop, chromosomePopCrossing, A, Sa, bestPop)
    fitnessValue = evaluate(chromosomePopCrossing, A, Sa)

    return chromosomeFinal, fitnessValue, A, Sa

#Permet d'effectuer l'algorithme génétique avec les opérations à effectuer dans l'ordre
def traitement(chromosomePop, A, Sa, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopulationCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength):
    #Evaluation
    fitnessValue = evaluate(chromosomePop, A, Sa)
    bestPop = positionBest(fitnessValue, bestPopLength)
    # Mutations
    chromosomePopMut = mutation(chromosomePop, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, bestPop, A, Sa)
    # Croisement
    chromosomePopCrossing = crossing(popNumber, chromosomePopMut, A, Sa, percentPopulationCrossing, lowPercentCutNumber, highPercentCutNumber, bestPop)

    chromosomePopFinal = betterOrNot(chromosomePop, chromosomePopCrossing, A, Sa, bestPop)
    return chromosomePopFinal, fitnessValue

#Permet d'afficher la liste des solutions trouvées
def solutionList(chromosomePop, fitnessValue):
    listOfSolutionIndexes = []
    for i in range(len(fitnessValue)):  #on itère sur tous les fitness value pour trouver les solutions
        if fitnessValue[i] == 0:
            listOfSolutionIndexes.append(i)
    listOfSolution = {}
    for i in range(len(listOfSolutionIndexes)):    #on récupère la valeur des solutions
        solution = chromosomePop[i]
        if solution not in listOfSolution.values():
            listOfSolution.update({listOfSolutionIndexes[i]: solution})
    return listOfSolution
