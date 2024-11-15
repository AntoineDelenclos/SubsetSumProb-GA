#This will allow to select a number of our best chromosomes from the population that we want to keep
def positionBest(fitnessValue, bestPopLength):
    # Trier les chromosomes par fitness croissante (meilleure fitness en premier)
    sortedFitness = [i for i, _ in sorted(fitnessValue.items(), key=lambda item: item[1])]
    bestIndexes = sortedFitness[:bestPopLength]
    #print(f"BEST : {fitnessValue[bestIndexes[0]]}")
    return bestIndexes

#This will retrieve the worst chromosomes in our population
def positionWorst(fitnessValue, worstPopLength):
    sortedFitness = [i for i, _ in sorted(fitnessValue.items(), key=lambda item: item[1], reverse=True)]
    worstIndexes = sortedFitness[:worstPopLength]
    return worstIndexes