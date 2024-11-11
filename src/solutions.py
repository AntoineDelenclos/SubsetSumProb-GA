import os
from multiprocessing import Pool
from src.traitement import firstTreatment, traitement, solutionList


def findSolutions(pathFile, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength, newFullyRandomBestLength, worstPopLength, penalty):
    # First population generation and treatment
    chromosomeFinal, fitnessValue, A, Sa = firstTreatment(pathFile, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength, penalty)

    min_value = min(fitnessValue.values())
    # Search of solution
    while min_value != 0:
        chromosomeFinal, fitnessValue = traitement(chromosomeFinal, A, Sa, popNumber, percentPopMutated,
                                                   lowPercentGenesMutated, highPercentGenesMutated,
                                                   percentPopCrossing, lowPercentCutNumber,
                                                   highPercentCutNumber, bestPopLength, newFullyRandomBestLength, worstPopLength, penalty)
        min_value = min(fitnessValue.values())

    listOfSolution = solutionList(chromosomeFinal, fitnessValue)
    print(listOfSolution)
    return listOfSolution

#This will find solutions for each file (we will use multiprocessing to speed up the process)
def folderSolutions(directory_path, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength, newFullyRandomBestLength, worstPopLength, penalty, cpuCores):
    txtFiles = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.txt')] #list of all the .txt contained inside our folder
    filesSolutions = {}
    numberFiles = len(txtFiles) # We will use that to know
    print(numberFiles)
    poolTasks = [(file, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength, newFullyRandomBestLength, worstPopLength, penalty) for file in txtFiles]

    with Pool(cpuCores) as pool: #This will allow for multiprocessing with all the available cores on our machine
        testPool = pool.starmap(findSolutions, poolTasks)

    count = 0
    for path in txtFiles:
        filesSolutions.update({os.path.basename(path): testPool[count]})
        count += 1

    return filesSolutions