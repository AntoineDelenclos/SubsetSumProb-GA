import random

#Permet de générer une population, initialise une population en fonction du nombre d'éléments dans le fichier
def ChromosomePopulationGeneration(PathA, populationNumber, popValueIs1Percent):
    global chromosomePopulation, Sa
    f = open(PathA, "r")
    A = []
    chromosomePopulation = []
    popValueIs0Percent = 1 - popValueIs1Percent
    for line in f:       #récupère les valeurs de A dans le fichier donné en paramètre
        if line[0] == "A":
            lineCharacters = line.split(" ")
            for ch in lineCharacters:
                if ch.isnumeric():
                    A.append(int(ch))
        else :           #récupère la valeur de sum(A)
            lineCharacters = line.split(" ")
            lineCharacters[2] = lineCharacters[2].replace("\n", "")
            for ch in lineCharacters:
                if ch.isnumeric():
                    Sa = int(ch)
    for i in range(populationNumber):       #créé des chromosomes en fonction de la taille de A
        if (popValueIs1Percent == 2):
            chromosome = [random.randint(0, 1) for j in range(len(A))]
        else:
            chromosome = [random.choices([0,1],[popValueIs0Percent, popValueIs1Percent])[0] for j in range(len(A))]
        chromosomePopulation.append(chromosome)
    return chromosomePopulation, A, Sa