def calculate_fitness(chromosome, A, Sa):
    # Initialize the fitness score
    fitness_score = 0

    E = 0
    for i in range(len(chromosome)):
        E += chromosome[i] * A[i]

    fitness_score += abs(E - Sa)

    return fitness_score

