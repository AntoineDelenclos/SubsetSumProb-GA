import os
from multiprocessing import Pool
from src.traitement import *


def findSolutions(pathFile, popNumber, popValueIs1Percent, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength, newFullyRandomBestLength, worstPopLength, penalty):
    # First population generation and treatment
    chromosomeFinal, fitnessValue, A, Sa = firstTreatment(
        pathFile, popNumber, popValueIs1Percent, percentPopMutated,
        lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing,
        lowPercentCutNumber, highPercentCutNumber, bestPopLength, penalty
    )
    numberTreatment = 1
    # Search of solution
    while (min_value := min(fitnessValue.values())) != 0:
        chromosomeFinal, fitnessValue = traitement(
            chromosomeFinal, A, Sa, popNumber, percentPopMutated,
            lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing,
            lowPercentCutNumber, highPercentCutNumber, bestPopLength,
            newFullyRandomBestLength, worstPopLength, penalty
        )
        numberTreatment += 1

    #print(f"Nombre de treatment: {numberTreatment}")

    return solutionList(chromosomeFinal, fitnessValue), numberTreatment

#This will find solutions for each file (we will use multiprocessing to speed up the process)
def folderSolutions(directory_path, popNumber, popValueIs1Percent, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber, bestPopLength, newFullyRandomBestLength, worstPopLength, penalty, cpuCores):
    txtFiles = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.txt')] #list of all the .txt contained inside our folder
    print(f"Le dossier {os.path.basename(directory_path)} contient {len(txtFiles)} fichiers.")
    #Preparing the task for multi-processing
    poolTasks = [
        (file, popNumber, popValueIs1Percent, percentPopMutated, lowPercentGenesMutated,
         highPercentGenesMutated, percentPopCrossing, lowPercentCutNumber, highPercentCutNumber,
         bestPopLength, newFullyRandomBestLength, worstPopLength, penalty)
        for file in txtFiles
    ]
    # Execution in parallel
    with Pool(cpuCores) as pool:
        exec = pool.starmap(findSolutions, poolTasks)
        results = [exec[i][0] for i in range(len(exec))]
        numberTreatmentsList = [exec[i][1] for i in range(len(exec))]

    # Associate solutions with file names
    filesSolutions = {
        os.path.basename(path): result
        for path, result in zip(txtFiles, results)
    }
    numberTreatments = {
        os.path.basename(txtFiles[i]): numberTreatmentsList[i]
        for i in range(len(txtFiles))
    }


    return filesSolutions, numberTreatments