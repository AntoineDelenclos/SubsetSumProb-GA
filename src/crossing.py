import random
from heapq import nsmallest
from src.fitnessFunction import calculate_fitness

def crossing(POPULATION_NUMBER, chromosomePop, A, Sa, percentPopulationCrossing, lowPercentCutNumber, highPercentCutNumber, bestPop, penalty):
    newChromosomePop = list(chromosomePop)
    populationCroisementNumber = int(percentPopulationCrossing * POPULATION_NUMBER)  # Croisement sur un pourcentage de la population
    countCroisements = 0
    while countCroisements < populationCroisementNumber:
        positionPopUn = random.randint(0, POPULATION_NUMBER - 1)   #on sélectionne un chromosome au hasard, l'autre aura 1 chance sur 2 d'être un meilleur chromosome
        while positionPopUn in bestPop:
            positionPopUn = random.randint(0,POPULATION_NUMBER - 1)
        bestChromosomeOrNot = random.randint(1,3)
        isBestChromosome = (bestChromosomeOrNot != 2)
        if bestChromosomeOrNot == 2:
            positionPopDeux = random.randint(0, POPULATION_NUMBER - 1)
            while positionPopDeux in bestPop:
                positionPopDeux = random.randint(0,POPULATION_NUMBER - 1)
        else :
            bestChromosomeChosen = random.randint(0, len(bestPop) - 1)
            positionPopDeux = bestPop[bestChromosomeChosen]

        chromosomeUn = chromosomePop[positionPopUn]
        chromosomeDeux = chromosomePop[positionPopDeux]

        CroisementNumberCut = random.randint(int(lowPercentCutNumber * len(chromosomeUn)),      #on choisit un nombre aléatoire de coupure en fonction de la taille du chromosome
                                             int(highPercentCutNumber * len(chromosomeUn)))
        chromosomeTrois = chromosomeUn.copy()

        lenCut = len(chromosomeUn) // CroisementNumberCut if CroisementNumberCut > 0 else 1 #on calcule la coupe de chaque chromosome
        lenCutLast = lenCut + len(chromosomeUn) % CroisementNumberCut if CroisementNumberCut > 0 else 1

        flip = random.randint(0, 1)

        for numberOfCut in range(CroisementNumberCut):
            if flip:
                if numberOfCut == CroisementNumberCut - 1:
                    for chromosomeChange in range(lenCutLast):
                        chromosomeIndex = numberOfCut * lenCut + chromosomeChange
                        chromosomeTrois[chromosomeIndex] = chromosomeDeux[chromosomeIndex]
                else:
                    for chromosomeChange in range(lenCut):
                        chromosomeIndex = numberOfCut * lenCut + chromosomeChange
                        chromosomeTrois[chromosomeIndex] = chromosomeDeux[chromosomeIndex]
                flip = False
            else:
                flip = True

        fitnessChromosomes = [
            (calculate_fitness(chromosomeUn, A, Sa, penalty), chromosomeUn),
            (calculate_fitness(chromosomeDeux, A, Sa, penalty), chromosomeDeux),
            (calculate_fitness(chromosomeTrois, A, Sa, penalty), chromosomeTrois)
        ]
        bestChromosomes = nsmallest(2, fitnessChromosomes, key=lambda x: x[0])

        if isBestChromosome and bestChromosomes[0][1] is chromosomeDeux:
            # Remettre chromosomeDeux dans sa position initiale si c'était le meilleur des trois
            newChromosomePop[positionPopDeux] = chromosomeDeux
        else:
            newChromosomePop[positionPopUn] = bestChromosomes[0][1]
            newChromosomePop[positionPopDeux] = bestChromosomes[1][1]

        countCroisements += 1
    return newChromosomePop


def relaxCrossing(POPULATION_NUMBER, chromosomePop, percentPopulationCrossing, percentCutNumber):
    newChromosomePop = list(chromosomePop)
    populationCrossingNumber = int(percentPopulationCrossing * POPULATION_NUMBER)  # Fewer crossovers applied
    countCrossings = 0

    while countCrossings < populationCrossingNumber:
        # Select two random chromosomes to cross
        positionPopOne = random.randint(0, POPULATION_NUMBER - 1)
        positionPopTwo = random.randint(0, POPULATION_NUMBER - 1)

        # Get the chromosomes to cross
        chromosomeOne = chromosomePop[positionPopOne]
        chromosomeTwo = chromosomePop[positionPopTwo]

        # Set a single crossover cut based on a percentage of the chromosome length
        crossoverPoint = int(percentCutNumber * len(chromosomeOne))

        # Create new chromosome by mixing parts of the selected chromosomes
        newChromosome = chromosomeOne[:crossoverPoint] + chromosomeTwo[crossoverPoint:]

        # Replace one of the chromosomes in the new population
        newChromosomePop[positionPopOne] = newChromosome

        countCrossings += 1

    return newChromosomePop