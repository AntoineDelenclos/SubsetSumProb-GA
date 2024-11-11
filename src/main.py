from src.solutions import folderSolutions

def main():
    # Training Settings
    POPULATION_NUMBER = 1000
    PERCENT_POP_MUTATED = 0.4
    LOW_PERCENT_GENES_MUTATED = 0.05
    HIGH_PERCENT_GENES_MUTATED = 0.2
    PERCENT_POP_CROSSING = 0.6
    LOW_PERCENT_CUT_NUMBER = 0.02
    HIGH_PERCENT_CUT_NUMBER = 0.8
    BEST_POP_LENGTH = 100

    smallSolutions = folderSolutions("C:/Users/antoi/PycharmProjects/SubsetSumProb-GA/data/small/", POPULATION_NUMBER, PERCENT_POP_MUTATED, LOW_PERCENT_GENES_MUTATED, HIGH_PERCENT_GENES_MUTATED, PERCENT_POP_CROSSING, LOW_PERCENT_CUT_NUMBER, HIGH_PERCENT_CUT_NUMBER, BEST_POP_LENGTH)
    #mediumSolutions = folderSolutions("C:/Users/antoi/PycharmProjects/SubsetSumProb-GA/data/medium/")
    #largeSolutions = folderSolutions("C:/Users/antoi/PycharmProjects/SubsetSumProb-GA/data/large/")
    #xlargeSolutions = folderSolutions("C:/Users/antoi/PycharmProjects/SubsetSumProb-GA/data/xlarge/")

    print(smallSolutions)

if __name__ == "__main__":
    main()
