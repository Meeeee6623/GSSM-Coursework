from random import choice

import numpy as np


def fitness(pop):
    return np.abs(pop - np.asarray([0, 1, 0, 1, 0]))


def generate_population(n):
    return np.random.random(n) > 0.5


def next_gen(pop, elite):
    new_gen = np.zeros(shape=pop.shape)
    np.random.shuffle(pop)
    elite = [elite[0], elite[1], elite[2]]
    for i, member in enumerate(pop[:-2]):
        if i < pop.size // 10:
            new_gen[i] = mutate(member)
        else:
            new_gen[i] = crossover(choice(elite), member)

    new_gen[-1] = elite[0]
    new_gen[-2] = elite[1]
    new_gen[-3] = elite[2]
    return new_gen


def mutate(p):
    r = np.random.randint(0, p.size)
    if p[r] == 0:
        p[r] = 1
    else:
        p[r] = 0
    return p


def crossover(p1, p2):
    return np.concatenate(p1[0:p1.size // 2], p2[p1.size // 2:])


population = generate_population(100)
scores = fitness(population)
top_3 = population[np.argpartition(scores, 3)]
print(top_3)
for i in range(100):
    population = next_gen(population, top_3)
    scores = fitness(population)
    top_3 = population[np.argpartition(scores, 3)]
