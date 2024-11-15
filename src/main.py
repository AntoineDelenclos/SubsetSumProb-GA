import time

from src.solutions import *
import os

def main():
    # Training Settings
    POPULATION_NUMBER = 50
    POPULATION_VALUE_IS_1_PERCENTAGE = 2 # Between 0 and 1 : you decide the percentage (random.choices), If == 2 : it uses random.randint
    PERCENT_POP_MUTATED = 0.3
    LOW_PERCENT_GENES_MUTATED = 0.01
    HIGH_PERCENT_GENES_MUTATED = 0.05
    PERCENT_POP_CROSSING = 0.8
    LOW_PERCENT_CUT_NUMBER = 0.1
    HIGH_PERCENT_CUT_NUMBER = 0.4
    BEST_POP_LENGTH = 15
    NEW_FULLY_RANDOM_POP_LENGTH = 2
    WORST_POP_LENGTH = BEST_POP_LENGTH + NEW_FULLY_RANDOM_POP_LENGTH
    PENALTY = 2

    CPU_CORES = os.cpu_count()  # Usefull for multiprocessing

    startTime = time.time()

    smallSolutions = folderSolutions("/home/antoine/PycharmProjects/SubsetSumProb-GA/data/small", POPULATION_NUMBER, POPULATION_VALUE_IS_1_PERCENTAGE, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH, NEW_FULLY_RANDOM_POP_LENGTH, WORST_POP_LENGTH, PENALTY, CPU_CORES)
    print(f"smallSolutions : {smallSolutions}")

    mediumSolutions = folderSolutions("/home/antoine/PycharmProjects/SubsetSumProb-GA/data/medium", POPULATION_NUMBER, POPULATION_VALUE_IS_1_PERCENTAGE, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH, NEW_FULLY_RANDOM_POP_LENGTH, WORST_POP_LENGTH, PENALTY, CPU_CORES)
    print(f"mediumSolutions : {mediumSolutions}")

    largeSolutions = folderSolutions("/home/antoine/PycharmProjects/SubsetSumProb-GA/data/large", POPULATION_NUMBER, POPULATION_VALUE_IS_1_PERCENTAGE, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH, NEW_FULLY_RANDOM_POP_LENGTH, WORST_POP_LENGTH, PENALTY, CPU_CORES)
    print(f"largeSolutions : {largeSolutions}")

    xlargeSolutions = folderSolutions("/home/antoine/PycharmProjects/SubsetSumProb-GA/data/xlarge", POPULATION_NUMBER, POPULATION_VALUE_IS_1_PERCENTAGE, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH, NEW_FULLY_RANDOM_POP_LENGTH, WORST_POP_LENGTH, PENALTY, CPU_CORES)
    print(f"xlargeSolutions : {xlargeSolutions}")

    endTime = time.time() - startTime
    print(f"Le temps total de calcul a pris : {endTime} secondes")

if __name__ == "__main__":
    main()
