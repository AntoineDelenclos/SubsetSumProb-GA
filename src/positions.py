#This will allow to select a number of our best chromosomes from the population that we want to keep
def positionBest(fitnessValue, bestPopLength):
    # Trier par fitness croissante et récupérer les `bestPopLength` premiers indices
    return sorted(fitnessValue, key=fitnessValue.get)[:bestPopLength]

#This will retrieve the worst chromosomes in our population
def positionWorst(fitnessValue, worstPopLength):
    # Trier par fitness décroissante et récupérer les `worstPopLength` premiers indices
    return sorted(fitnessValue, key=fitnessValue.get, reverse=True)[:worstPopLength]
