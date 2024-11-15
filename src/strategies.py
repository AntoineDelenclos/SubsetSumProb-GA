import random
from src.fitnessFunction import calculate_fitness


def betterOrNot(chromosomePopBeforeCrossing, chromosomePopAfterCrossing, A, Sa, bestPop, penalty):
    # Parcourir chaque index des meilleurs chromosomes
    for idx in bestPop:
        fitness_before = calculate_fitness(chromosomePopBeforeCrossing[idx], A, Sa, penalty)
        fitness_after = calculate_fitness(chromosomePopAfterCrossing[idx], A, Sa, penalty)

        # Remplacement si le score de fitness s'améliore ou reste constant
        if fitness_before <= fitness_after:
            chromosomePopAfterCrossing[idx] = chromosomePopBeforeCrossing[idx]
    return chromosomePopAfterCrossing


def strategyWorst(chromosomePopPreFinal, A, bestPop, worstPop, newFullyRandomBestLength, lowPercentGenesMutated, highPercentGenesMutated):
    chromosomePopFinal = chromosomePopPreFinal.copy()
    replacementChromosomePop = []

    for i in range(newFullyRandomBestLength): #generate new chromosomes
        chromosome = [random.randint(0, 1) for j in range(len(A))]
        replacementChromosomePop.append(chromosome)

    for i in range(len(bestPop)): #do the mutation of the best chromosomes
        chromosome = chromosomePopPreFinal[bestPop[i]].copy()
        geneNumberTransformed = random.randint(int(lowPercentGenesMutated * len(chromosome)), int(highPercentGenesMutated * len(chromosome)))  # Between X and Y % of genes mutated
        specificTransformedGenes = [random.randint(0, len(chromosome) - 1) for i in range(geneNumberTransformed)]  # Select genes to mutate
        for geneIndex in specificTransformedGenes:
            chromosome[geneIndex] = (chromosome[geneIndex] + 1) % 2  # Flip the gene value between 0 and 1

        replacementChromosomePop.append(chromosome)

    count = 0
    for idx in worstPop: #replace the worsts by new chromosomes
        chromosomePopFinal[idx] = replacementChromosomePop[count]
        count += 1

    return chromosomePopFinal