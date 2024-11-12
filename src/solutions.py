import os
from multiprocessing import Pool
from src.traitement import *


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


def relaxFindSolutions(pathFile, popNumber, percentPopMutated, percentGenesMutated, percentPopCrossing,
                       percentCutNumber,
                       bestPopLength, newFullyRandomBestLength, worstPopLength, penalty):
    # Initial population generation and relaxed treatment
    chromosomeFinal, fitnessValue, A, Sa = firstTreatment(pathFile, popNumber, percentPopMutated,
                                                          percentGenesMutated, percentGenesMutated,
                                                          percentPopCrossing, percentCutNumber,
                                                          percentCutNumber, bestPopLength, penalty)

    min_value = min(fitnessValue.values())

    # Iteratively apply relaxed treatment until a solution is found
    while min_value != 0:
        chromosomeFinal, fitnessValue = traitementRelax(chromosomeFinal, A, Sa, popNumber,
                                                        percentPopMutated, percentGenesMutated,
                                                        percentGenesMutated, percentPopCrossing,
                                                        percentCutNumber, percentCutNumber, bestPopLength,
                                                        newFullyRandomBestLength, worstPopLength, penalty)
        min_value = min(fitnessValue.values())

    listOfSolution = solutionList(chromosomeFinal, fitnessValue)
    print(listOfSolution)
    return listOfSolution


def relaxFolderSolutions(directory_path, popNumber, percentPopMutated, percentGenesMutated, percentPopCrossing,
                         percentCutNumber, bestPopLength, newFullyRandomBestLength, worstPopLength, penalty, cpuCores):
    # List of all .txt files in the directory
    txtFiles = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.txt')]
    filesSolutions = {}
    numberFiles = len(txtFiles)
    print(f"Number of files to process: {numberFiles}")

    # Prepare tasks for multiprocessing, using the relaxed parameters
    poolTasks = [(file, popNumber, percentPopMutated, percentGenesMutated, percentPopCrossing, percentCutNumber,
                  bestPopLength, newFullyRandomBestLength, worstPopLength, penalty) for file in txtFiles]

    # Use multiprocessing to apply relaxFindSolutions to each file in the directory
    with Pool(cpuCores) as pool:
        testPool = pool.starmap(relaxFindSolutions, poolTasks)

    # Collect solutions for each file
    for idx, path in enumerate(txtFiles):
        filesSolutions[os.path.basename(path)] = testPool[idx]

    return filesSolutions