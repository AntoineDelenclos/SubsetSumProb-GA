import random


def ChromosomePopulationGeneration(PathA, populationNumber):
    global chromosomePopulation, Sa
    f = open(PathA, "r")
    A = []
    for line in f:
        if line[0] == "A":
            lineCharacters = line.split(" ")
            for ch in lineCharacters:
                if ch.isnumeric():
                    A.append(int(ch))
        else :
            lineCharacters = line.split(" ")
            lineCharacters[2] = lineCharacters[2].replace("\n", "")
            for ch in lineCharacters:
                if ch.isnumeric():
                    Sa = int(ch)
        chromosomePopulation = []
    for i in range(populationNumber):
        chromosome = [random.randint(0, 1) for j in range(len(A))]
        chromosomePopulation.append(chromosome)
    return chromosomePopulation, A, Sa