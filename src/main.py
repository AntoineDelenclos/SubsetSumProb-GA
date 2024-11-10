import random
from heapq import nsmallest, nlargest

from ChromosomePopulationGenerator import ChromosomePopulationGeneration
from fitnessFunction import calculate_fitness


def main():
    path = "/home/quentin/Documents/Polytech/Semestre9/Traitement-automatique-des-langues/SubsetSumProb-GA/data/small/ssp_small_1_pbm.txt"
    # Generation de la premiere population
    POPULATION_NUMBER = 1000
    chromosomePop, A, Sa = ChromosomePopulationGeneration(path, POPULATION_NUMBER)
    tenBest = []
    tenWorst = []
    fitnessValue = []
    fitnessPosition = {}
    for chromosome in chromosomePop:
        fitness = calculate_fitness(chromosome, A, Sa)
        fitnessValue.append(fitness)
        fitnessPosition[tuple(chromosome)] = fitness
        print(fitness)

    # 10 best
    tenBest = nsmallest(10, fitnessValue)
    tenWorst = nlargest(10, fitnessValue)
    print(fitnessPosition)

    # Mutations
    populationMutationNumber = int(0.2 * POPULATION_NUMBER)  # Mutation sur 20% de la population
    countMutations = 0
    while countMutations < populationMutationNumber:
        positionPop = random.randint(0, POPULATION_NUMBER - 1)
        chromosome = chromosomePop[positionPop]
        geneNumberTransformed = random.randint(int(0.1 * len(chromosome)),
                                               int(0.4 * len(chromosome)))  # Between 10% and 40% of genes mutated
        specificTransformedGenes = [random.randint(0, len(chromosome) - 1) for _ in
                                    range(geneNumberTransformed)]  # Select genes to mutate

        print(f"count: {countMutations}, chromosome before mutation: {chromosome}")

        for geneIndex in specificTransformedGenes:
            chromosome[geneIndex] = (chromosome[geneIndex] + 1) % 2  # Flip the gene value between 0 and 1
        chromosomePop[positionPop] = chromosome
        print(f"count: {countMutations}, chromosome after mutation: {chromosome}")
        countMutations += 1

    # Croisement
    populationCroisementNumber = int(0.35 * POPULATION_NUMBER)  # Croisement sur 35% de la population
    countCroisements = 0
    while countCroisements < populationCroisementNumber:
        positionPopUn = random.randint(0, POPULATION_NUMBER - 1)
        positionPopDeux = random.randint(0, POPULATION_NUMBER - 1)
        chromosomeUn = chromosomePop[positionPopUn]
        chromosomeDeux = chromosomePop[positionPopDeux]
        random.randint(1,4)
        CroisementNumberCut = random.randint(int(0.1 * len(chromosomeUn)),              #Nombre d'endroit ou il va y avoir des croisements (entre 10 et 40%)
                                               int(0.4 * len(chromosomeUn)))
        chromosomeTrois = chromosomeUn.copy()

        lenCut = len(chromosomeUn)//CroisementNumberCut                 #longueur des coupures du croisement
        flip = random.randint(0, 1)
        for  numberOfCut in range (0,CroisementNumberCut):              #sur l'ensemble des coupures
            if flip :                                                   #soit on modifie une partie du code en remplacement par chromosome deux
                for chromosomeChange in range (0,lenCut):
                    chromosomeIndex = numberOfCut*lenCut+chromosomeChange+1
                    chromosomeTrois.insert(chromosomeIndex, chromosomeDeux[chromosomeChange])
                flip = False
            else :                                                      #soit rien n'est fait
                flip = True
        fitnessMinimal = [calculate_fitness(chromosomeUn, A, Sa), calculate_fitness(chromosomeDeux, A, Sa), calculate_fitness(chromosomeTrois, A, Sa)]      #on calcule le fitness des trois chromosomes
        chromosomeChoose = nsmallest(2, fitnessMinimal)
        chromosomePop[positionPopUn] = chromosomeChoose[0]
        chromosomePop[positionPopDeux] = chromosomeChoose[1]            #on modifie les deux chromosomes avec le meilleur croisement


    # #Boucle jusqu'à temps que résolu
    # while (1 == 1):
    #
    #
    #     #Scoring
    #    #for chromosome in chromosomePop:
    #      #  calculate_fitness(chromosome, A, Sa)


if __name__ == "__main__":
    main()
