def calculate_fitness(chromosome, A, Sa, penalty): #A is the set and Sa the targeted value
    fitness_score = 0

    E = 0 #Weighted sum
    for i in range(len(chromosome)):
        E += chromosome[i] * A[i]

    if E > Sa: #If we overshoot the targeted value we need to penalize the solution
        fitness_score += abs(E - Sa) + penalty
    else:
        fitness_score += abs(E - Sa)

    return fitness_score

def evaluate(chromosomePop, A, Sa, penalty):
    fitnessValue = {} #Dictionnary that will store the position of the chromosome in the population and linked it with its fitness value
    count = 0
    for chromosome in chromosomePop:
        fitness = calculate_fitness(chromosome, A, Sa, penalty)
        fitnessValue.update({count: fitness})
        count += 1
    return fitnessValue

#This will allow to select a number of our best chromosomes from the population that we want to keep
def positionBest(fitnessValue, bestPopLength):
    # Trier les chromosomes par fitness croissante (meilleure fitness en premier)
    sortedFitness = [i for i, _ in sorted(fitnessValue.items(), key=lambda item: item[1])]
    bestIndexes = sortedFitness[:bestPopLength]
    print(f"BEST : {fitnessValue[bestIndexes[0]]}")
    return bestIndexes


def betterOrNot(chromosomePopBeforeCrossing, chromosomePopAfterCrossing, A, Sa, bestPop, penalty):
    # Parcourir chaque index des meilleurs chromosomes
    for idx in bestPop:
        fitness_before = calculate_fitness(chromosomePopBeforeCrossing[idx], A, Sa, penalty)
        fitness_after = calculate_fitness(chromosomePopAfterCrossing[idx], A, Sa, penalty)

        # Remplacement si le score de fitness s'améliore ou reste constant
        if fitness_before <= fitness_after:
            chromosomePopAfterCrossing[idx] = chromosomePopBeforeCrossing[idx]
    return chromosomePopAfterCrossing
