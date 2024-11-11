import random

#Permet de générer une population, initialise une population en fonction du nombre d'éléments dans le fichier
def ChromosomePopulationGeneration(PathA, populationNumber):
    global chromosomePopulation, Sa
    f = open(PathA, "r")
    A = []
    chromosomePopulation = []
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
        chromosome = [random.randint(0, 1) for j in range(len(A))]
        chromosomePopulation.append(chromosome)
    return chromosomePopulation, A, Sa