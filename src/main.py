from src.solutions import folderSolutions
import os

def main():
    # Training Settings
    POPULATION_NUMBER = 30000
    PERCENT_POP_MUTATED = 0.4
    LOW_PERCENT_GENES_MUTATED = 0.05
    HIGH_PERCENT_GENES_MUTATED = 0.2
    PERCENT_POP_CROSSING = 0.6
    LOW_PERCENT_CUT_NUMBER = 0.02
    HIGH_PERCENT_CUT_NUMBER = 0.8
    BEST_POP_LENGTH = 100
    CPU_CORES = os.cpu_count() #Usefull for multiprocessing

    #smallSolutions = folderSolutions("C:/Users/antoi/PycharmProjects/SubsetSumProb-GA/data/small/", POPULATION_NUMBER, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH, CPU_CORES)
    #print(f"smallSolutions : {smallSolutions}")

    #mediumSolutions = folderSolutions("C:/Users/antoi/PycharmProjects/SubsetSumProb-GA/data/medium/", POPULATION_NUMBER, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH, CPU_CORES)
    #print(f"mediumSolutions : {mediumSolutions}")

    largeSolutions = folderSolutions("C:/Users/antoi/PycharmProjects/SubsetSumProb-GA/data/large/", POPULATION_NUMBER, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH, CPU_CORES)
    print(f"largeSolutions : {largeSolutions}")

    #xlargeSolutions = folderSolutions("C:/Users/antoi/PycharmProjects/SubsetSumProb-GA/data/xlarge/", POPULATION_NUMBER, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH, CPU_CORES)
    #print(f"xlargeSolutions : {xlargeSolutions}")


if __name__ == "__main__":
    main()
