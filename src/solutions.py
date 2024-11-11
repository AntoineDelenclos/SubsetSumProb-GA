import os
from src.traitement import firstTreatment, traitement, solutionList


def findSolutions(pathFile, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength):
    # First population generation and treatment
    chromosomeFinal, fitnessValue, A, Sa = firstTreatment(pathFile, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength)

    # Search of solution
    while min(fitnessValue.values()) > 0:
        chromosomeFinal, fitnessValue = traitement(chromosomeFinal, A, Sa, popNumber, percentPopMutated,
                                                   lowPercentGenesMutated, highPercentGenesMutated,
                                                   percentPopCrossing, lowPercentCutNumber,
                                                   highPercentCutNumber, bestPopLength)

    listOfSolution = solutionList(chromosomeFinal, fitnessValue)
    print(listOfSolution)
    return listOfSolution

def folderSolutions(directory_path, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength):
    txtFiles = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.txt')] #list of all the .txt contained inside our folder
    filesSolutions = {}
    for path in txtFiles:
        listOfSolutions = findSolutions(path, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength)
        filesSolutions.update({os.path.basename(path): listOfSolutions})
    return filesSolutions