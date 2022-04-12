from random import choice

import numpy as np

NUM_GENOMES = 40
POP_SIZE = 100

OPTIMAL = np.asarray([[1] * NUM_GENOMES][0])


def fitness(pop):
    return np.sum(pop == OPTIMAL, axis=1)


def generate_population(n):
    pop = np.zeros((n, NUM_GENOMES))
    mask = np.random.rand(n, NUM_GENOMES) < 0.5
    pop[mask] = 0
    return pop


def next_gen(pop, elite):
    new_gen = np.zeros(shape=pop.shape)
    np.random.shuffle(pop)
    elite = [elite[0], elite[1], elite[2]]
    for i, member in enumerate(pop[:-2]):
        if i < pop.size // 20:
            new_gen[i] = mutate(member)
        else:
            new_gen[i] = crossover(choice(elite), member)

    new_gen[-1] = elite[0]
    new_gen[-2] = elite[1]
    new_gen[-3] = elite[2]
    return new_gen


def mutate(p):
    r = np.random.randint(0, NUM_GENOMES)
    if p[r] == 0:
        p[r] = 1
    else:
        p[r] = 0
    return p


def crossover(elite, p2):
    r = np.random.randint(0, NUM_GENOMES)
    return np.concatenate([elite[0:r], p2[r:]])


convergence = []
for gen in range(5):
    population = generate_population(POP_SIZE)
    scores = fitness(population)
    top_3 = population[np.argpartition(scores, -3)[-3:]]
    i = 2
    while ~np.any(scores == 20):
        population = next_gen(population, top_3)
        scores = fitness(population)
        top_3 = population[np.argpartition(scores, -3)[-3:]]
        i += 1
    print(f'Converged at generation {i}')
    convergence.append(i)
print(f'Average Convergence: {np.mean(convergence)}')
