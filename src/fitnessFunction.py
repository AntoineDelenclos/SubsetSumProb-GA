def calculate_fitness(chromosome, A, Sa):
    fitness_score = 0

    E = 0
    for i in range(len(chromosome)):
        E += chromosome[i] * A[i]

    fitness_score += abs(E - Sa)

    return fitness_score

def evaluate(chromosomePop, A, Sa):
    fitnessValue = {} #Dictionnary that will store the position of the chromosome in the population and linked it with its fitness value
    count = 0
    for chromosome in chromosomePop:
        fitness = calculate_fitness(chromosome, A, Sa)
        fitnessValue.update({count: fitness})
        count += 1
    return fitnessValue

#This will allow to select a number of our best chromosomes from the population that we want to keep
def positionBest(fitnessValue, bestPopLength):
    #sortedFitness = dict(sorted(fitnessValue.items(), key=lambda item: item[1]))
    sortedFitness = [i for i, j in sorted(fitnessValue.items(), key=lambda item: item[1])]
    #print(sortedFitness)
    bestIndexes = []
    for i in range(bestPopLength):
        bestIndexes.append(sortedFitness[i])
        #bestIndexes.append(sortedFitness[i][0])
    #print(bestIndexes)
    print(f"BEST : {fitnessValue[bestIndexes[0]]}")
    return bestIndexes

def betterOrNot(chromosomePopBeforeCrossing, chromosomePopAfterCrossing, A, Sa, bestPop):
    for i in range(len(bestPop)):
        if calculate_fitness(chromosomePopBeforeCrossing[bestPop[i]], A, Sa) < calculate_fitness(chromosomePopAfterCrossing[bestPop[i]], A, Sa):
            chromosomePopAfterCrossing[bestPop[i]] = chromosomePopBeforeCrossing[bestPop[i]]
    return chromosomePopAfterCrossing