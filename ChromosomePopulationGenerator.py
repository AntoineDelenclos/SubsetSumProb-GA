import random
import sys

OUTPUT_PATH = "ChromosomePopulation"

POPULATION_NUMBER = 1000

chromosome_composition = {
    "EffDistOPP2WinBeforeUsingWall": [1,25],
    "Dist2WinXRatioHazardToLose": [1,100],
    "PutAWallIfIncreasesOpponentPath": [0,2], #0 Never; 1 Mandatory; 2 Only if path not increase for us
    "PointsBehindToTriggerBlockingOpponent": [0,50],
    "MovingOrWall": [0,1] #0 Moving; 1 Wall
}

# print(chromosome_composition.values)

def ChromosomePopulationGeneration(A):
    chromosomePopulation = []
    for i in range(POPULATION_NUMBER):
        chromosome = [random.randint(0, 1) for j in range(len(A))]
        chromosomePopulation.append(chromosome)
    return chromosomePopulation

# print("Which Player will have this population ?")
player = sys.stdin.readline()
player = player.rstrip("\n")
player = int(player)
# print("How much chromosome in your population ?")
populationNumber = sys.stdin.readline()
populationNumber = populationNumber.rstrip("\n")
populationNumber = int(populationNumber)
f = open(str(OUTPUT_PATH+"{}".format(player)+".txt"),"w")
chromosomePopulation = ChromosomePopulationGeneration(population_number=populationNumber)
f.write(str(chromosomePopulation))
f.close()
