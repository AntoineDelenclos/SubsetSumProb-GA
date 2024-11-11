import random
from src.fitnessFunction import calculate_fitness

def mutation(chromosomePop, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, bestPop, A, Sa, penalty):
    populationMutationNumber = int(percentPopMutated * popNumber)  #A % of our population will be mutated
    countMutations = 0
    newChromosomePop = chromosomePop.copy()
    while countMutations < populationMutationNumber:
        positionPop = random.randint(0, popNumber - 1)
        while positionPop in bestPop:
            positionPop = random.randint(0, popNumber - 1)
        chromosome = newChromosomePop[positionPop]
        geneNumberTransformed = random.randint(int(lowPercentGenesMutated * len(chromosome)), int(highPercentGenesMutated * len(chromosome)))  # Between X and Y % of genes mutated
        specificTransformedGenes = [random.randint(0, len(chromosome) - 1) for i in range(geneNumberTransformed)]  # Select genes to mutate

        for geneIndex in specificTransformedGenes:
            chromosome[geneIndex] = (chromosome[geneIndex] + 1) % 2  # Flip the gene value between 0 and 1

        if calculate_fitness(chromosome, A, Sa, penalty) < calculate_fitness(newChromosomePop[positionPop], A, Sa, penalty): #We only keep the mutation if it improves the fitness
            newChromosomePop[positionPop] = chromosome

        countMutations += 1
    #we mutate the best population together
    for positionPop in bestPop:
        chromosome = newChromosomePop[positionPop]
        geneNumberTransformed = random.randint(int(lowPercentGenesMutated * len(chromosome)),
                                               int(highPercentGenesMutated * len(chromosome)))
        specificTransformedGenes = [random.randint(0, len(chromosome) - 1) for i in range(geneNumberTransformed)]

        # Apply mutation
        mutatedChromosome = chromosome.copy()
        for geneIndex in specificTransformedGenes:
            mutatedChromosome[geneIndex] = (mutatedChromosome[geneIndex] + 1) % 2

        # Check if mutated chromosome is better
        original_fitness = calculate_fitness(chromosome, A, Sa, penalty)
        mutated_fitness = calculate_fitness(mutatedChromosome, A, Sa, penalty)
        if mutated_fitness < original_fitness:
            newChromosomePop[positionPop] = mutatedChromosome  # Keep the mutation if it's better

    return newChromosomePop
