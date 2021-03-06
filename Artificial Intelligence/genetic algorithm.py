from random import choice
import matplotlib.pyplot as plt
import numpy as np


def fitness(pop):
    return np.sqrt((pop[:, 0] - 0.5) ** 2 + (pop[:, 1] - 0.5) ** 2)


def generate_population(n):
    return np.random.rand(n, 2)


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
    r = np.random.random()
    if r < .25:
        return p[0] + r / 50, p[1]
    elif r < .5:
        return p[0] - r / 50, p[1]
    elif r < .75:
        return p[0], p[1] + r / 50
    else:
        return p[0], p[1] - r / 50


def crossover(p1, p2):
    if np.random.random() > .5:
        return p1[0], p2[1]
    else:
        return p2[0], p1[1]


population = generate_population(100)
scores = fitness(population)
top_3 = population[np.argpartition(scores, 3)]
print(top_3)
for i in range(100):
    population = next_gen(population, top_3)
    scores = fitness(population)
    top_3 = population[np.argpartition(scores, 3)]
    plt.scatter(population[:, 0], population[:, 1])
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.xticks(np.linspace(0, 1, 11))
    plt.yticks(np.linspace(0, 1, 11))
    plt.grid()
    plt.savefig(rf'images\gen_{i}.png')
    plt.show()

