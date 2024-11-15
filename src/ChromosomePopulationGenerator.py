import random

#Permet de générer une population, initialise une population en fonction du nombre d'éléments dans le fichier
def ChromosomePopulationGeneration(PathA, populationNumber, popValueIs1Percent):
    # Lire le fichier et récupérer les valeurs de A et Sa
    with open(PathA, "r") as f:
        A = []
        Sa = None

        for line in f:
            if line.startswith("A"):  # Ligne contenant A -> début des valeurs
                A += [int(ch) for ch in line.split() if ch.isnumeric()]
            else:  # Ligne contenant Sa -> valeur à atteindre
                Sa = next(int(ch) for ch in line.split() if ch.isnumeric())

    # Générer les chromosomes
    popValueIs0Percent = 1 - popValueIs1Percent
    chromosomePopulation = [
        [
            random.randint(0, 1) if popValueIs1Percent == 2
            else random.choices([0, 1], [popValueIs0Percent, popValueIs1Percent])[0]
            for _ in range(len(A))
        ]
        for _ in range(populationNumber)
    ]
    return chromosomePopulation, A, Sa