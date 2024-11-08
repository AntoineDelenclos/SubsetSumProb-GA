def calculate_fitness(chromosome, A, Sa):
    # Initialize the fitness score
    fitness_score = 0

    E = 0
    for i in range(len(chromosome)):
        E += chromosome[i] * A[i]

    fitness_score += abs(E - Sa)

    return fitness_score

#Si on a le temps peut etre essayer de trouver la meilleure solution en ayant le cardinal de A* le plus faible (donc le chromosome avec le moins de 1 possible)

