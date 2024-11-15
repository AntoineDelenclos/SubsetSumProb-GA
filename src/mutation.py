import random
from src.fitnessFunction import calculate_fitness

def mutation(chromosomePop, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, bestPop, A, Sa, penalty):
    populationMutationNumber = int(percentPopMutated * popNumber)  #A % of our population will be mutated
    newChromosomePop = chromosomePop.copy()
    mutatedIndices = set()

    # Mutation des chromosomes hors de la meilleure population
    while len(mutatedIndices) < populationMutationNumber:
        positionPop = random.randint(0, popNumber - 1)
        if positionPop in bestPop or positionPop in mutatedIndices:
            continue

        chromosome = newChromosomePop[positionPop].copy()
        geneNumberTransformed = random.randint(
            int(lowPercentGenesMutated * len(chromosome)),
            int(highPercentGenesMutated * len(chromosome))
        )
        specificTransformedGenes = random.sample(range(len(chromosome)), geneNumberTransformed)

        # Mutation des gènes
        for geneIndex in specificTransformedGenes:
            chromosome[geneIndex] = 1 - chromosome[geneIndex]  # Bascule entre 0 et 1

        # Garder la mutation si elle améliore la fitness
        if calculate_fitness(chromosome, A, Sa, penalty) < calculate_fitness(newChromosomePop[positionPop], A, Sa,
                                                                             penalty):
            newChromosomePop[positionPop] = chromosome

        mutatedIndices.add(positionPop)

    # Mutation des chromosomes de la meilleure population
    for positionPop in bestPop:
        chromosome = newChromosomePop[positionPop].copy()
        geneNumberTransformed = random.randint(
            int(lowPercentGenesMutated * len(chromosome)),
            int(highPercentGenesMutated * len(chromosome))
        )
        specificTransformedGenes = random.sample(range(len(chromosome)), geneNumberTransformed)

        # Mutation des gènes
        mutatedChromosome = chromosome.copy()
        for geneIndex in specificTransformedGenes:
            mutatedChromosome[geneIndex] = 1 - mutatedChromosome[geneIndex]

        # Garder la mutation si elle améliore la fitness
        if calculate_fitness(mutatedChromosome, A, Sa, penalty) < calculate_fitness(chromosome, A, Sa, penalty):
            newChromosomePop[positionPop] = mutatedChromosome

    return newChromosomePop