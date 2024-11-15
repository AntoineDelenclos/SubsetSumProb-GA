import random

def calculate_fitness(chromosome, A, Sa, penalty): #A is the set and Sa the targeted value
    E = sum(gene * weight for gene, weight in zip(chromosome, A)) #Weighted sum

    fitness_score = abs(E - Sa) + (penalty if E > Sa else 0) #fitness score depending on the penality

    return fitness_score

def evaluate(chromosomePop, A, Sa, penalty):
    fitnessValue = {
        idx: calculate_fitness(chromosome, A, Sa, penalty)
        for idx, chromosome in enumerate(chromosomePop)
    } #Dictionnary that will store the position of the chromosome in the population and linked it with its fitness value
    return fitnessValue