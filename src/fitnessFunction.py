import random

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