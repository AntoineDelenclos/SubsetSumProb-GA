import random
from src.fitnessFunction import calculate_fitness


def betterOrNot(chromosomePopBeforeCrossing, chromosomePopAfterCrossing, A, Sa, bestPop, penalty):
    # Parcourir chaque index des meilleurs chromosomes et remplacement si plus intéressant ou non
    for idx in bestPop:
        if calculate_fitness(chromosomePopBeforeCrossing[idx], A, Sa, penalty) <= calculate_fitness(
                chromosomePopAfterCrossing[idx], A, Sa, penalty):
            chromosomePopAfterCrossing[idx] = chromosomePopBeforeCrossing[idx]
    return chromosomePopAfterCrossing


def strategyWorst(chromosomePopPreFinal, A, bestPop, worstPop, newFullyRandomBestLength, lowPercentGenesMutated, highPercentGenesMutated):
    chromosomePopFinal = chromosomePopPreFinal.copy()
    #generate new random chromosomes
    replacementChromosomePop = [
        [random.randint(0, 1) for _ in range(len(A))]
        for _ in range(newFullyRandomBestLength)
    ]

    for idx in bestPop:
        chromosome = chromosomePopPreFinal[idx].copy()
        # Compute the number of genes to mutate
        geneNumberTransformed = random.randint(
            int(lowPercentGenesMutated * len(chromosome)),
            int(highPercentGenesMutated * len(chromosome))
        )
        # Random selection of mutation indexes
        specificTransformedGenes = random.sample(range(len(chromosome)), geneNumberTransformed)
        # Mutation of selectionned genes
        for geneIndex in specificTransformedGenes:
            chromosome[geneIndex] = 1 - chromosome[geneIndex]  # Bascule entre 0 et 1
        replacementChromosomePop.append(chromosome)

        # Remplacement worst chromosomes
    for count, idx in enumerate(worstPop):
        chromosomePopFinal[idx] = replacementChromosomePop[count]

    return chromosomePopFinal