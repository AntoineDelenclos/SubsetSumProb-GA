import random

def mutation(chromosomePop, popNumber, percentPopMutated, lowPercentGenesMutated, highPercentGenesMutated, bestPop):
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
        newChromosomePop[positionPop] = chromosome
        countMutations += 1
    return newChromosomePop
