import matplotlib.pyplot as plt
import numpy as np


def fitness(pop):
    return np.sqrt((pop[:, 0] - .5) ** 2 + (pop[:, 1] - .5) ** 2)


def generate_population(n):
    return np.random.rand(n, 2)


def next_gen(pop, elite):
    new_gen = np.zeros(shape=pop.shape)
    for i, member in enumerate(np.random.shuffle(pop)):
        if i < 4:
            new_gen[i] = mutate(member)
        else:
            new_gen[i] = crossover(elite, member)

    new_gen[-1] = elite
    return new_gen


def mutate(p):
    if np.random.random() > .5:
        return np.random.random(), p[1]
    else:
        return p[0], np.random.random()


def crossover(p1, p2):
    if np.random.random() > .5:
        return p1[0], p2[1]
    else:
        return p2[0], p1[1]


population = generate_population(10)
scores = fitness(population)
most_fit = population[np.argmin(scores)]
for _ in range(4):
    population = next_gen(population, most_fit)
    plt.plot(population[:, 0], population[:, 1])
