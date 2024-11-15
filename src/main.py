import time

from src.solutions import *
import os

def main():
    # Training Settings
    POPULATION_NUMBER = 50  # Plus petit pour moins de calculs
    PERCENT_POP_MUTATED = 0.3  # Réduire pour limiter les variations aléatoires
    LOW_PERCENT_GENES_MUTATED = 0.01  # Moins de gènes modifiés
    HIGH_PERCENT_GENES_MUTATED = 0.05  # Mutation contrôlée
    PERCENT_POP_CROSSING = 0.8  # Plus de croisements pour exploiter les solutions
    LOW_PERCENT_CUT_NUMBER = 0.1  # Coupures réduites pour préserver des solutions
    HIGH_PERCENT_CUT_NUMBER = 0.4  # Coupures modérées
    BEST_POP_LENGTH = 15  # Conserver plus des meilleures solutions
    NEW_FULLY_RANDOM_POP_LENGTH = 2  # Réduire les individus aléatoires
    WORST_POP_LENGTH = BEST_POP_LENGTH + NEW_FULLY_RANDOM_POP_LENGTH  # Ajuster
    PENALTY = 2  # Réduire pour éviter de trop pénaliser les solutions imparfaites

    CPU_CORES = os.cpu_count()  # Usefull for multiprocessing

    startTime = time.time()

    smallSolutions = folderSolutions("/home/antoine/PycharmProjects/SubsetSumProb-GA/data/small", POPULATION_NUMBER, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH, NEW_FULLY_RANDOM_POP_LENGTH, WORST_POP_LENGTH, PENALTY, CPU_CORES)
    print(f"smallSolutions : {smallSolutions}")

    mediumSolutions = folderSolutions("/home/antoine/PycharmProjects/SubsetSumProb-GA/data/medium", POPULATION_NUMBER, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH, NEW_FULLY_RANDOM_POP_LENGTH, WORST_POP_LENGTH, PENALTY, CPU_CORES)
    print(f"mediumSolutions : {mediumSolutions}")

    largeSolutions = folderSolutions("/home/antoine/PycharmProjects/SubsetSumProb-GA/data/large", POPULATION_NUMBER, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH, NEW_FULLY_RANDOM_POP_LENGTH, WORST_POP_LENGTH, PENALTY, CPU_CORES)
    print(f"largeSolutions : {largeSolutions}")

    xlargeSolutions = folderSolutions("/home/antoine/PycharmProjects/SubsetSumProb-GA/data/xlarge", POPULATION_NUMBER, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH, NEW_FULLY_RANDOM_POP_LENGTH, WORST_POP_LENGTH, PENALTY, CPU_CORES)
    print(f"xlargeSolutions : {xlargeSolutions}")

    endTime = time.time() - startTime
    print(f"Le temps total de calcul a pris : {endTime} secondes")

if __name__ == "__main__":
    main()
