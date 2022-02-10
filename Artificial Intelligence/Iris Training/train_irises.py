'''Iris Classification with multiple distance metrics
Author: Benjamin Chauhan'''
import numpy as np


def classify(distances: list):
    setosa_dist = distances[0]
    versicolor_dist = distances[1]
    virginica_dist = distances[2]
    # boolean array of correct vs. false classifications
    classifications = np.concatenate([setosa_dist[0:10] < np.minimum(versicolor_dist[0:10], virginica_dist[0:10]),
                                      versicolor_dist[10:20] < np.minimum(setosa_dist[10:20], virginica_dist[10:20]),
                                      virginica_dist[20:] < np.minimum(versicolor_dist[20:], setosa_dist[20:])])

    correct = np.count_nonzero(classifications)
    wrong = len(setosa_dist) - correct
    wrong_indexes = np.where(~classifications)[0]
    print(f'Accuracy: {np.round(correct / len(setosa_dist), 3)}%')
    print(f'{correct} Irises were correctly classified.')
    print(f'{wrong} Irises were incorrectly classified:')
    for i in wrong_indexes:
        iris_types = ['setosa', 'versicolor', 'virginica']
        nearest_dist = np.round(np.amin(np.array([setosa_dist[i], versicolor_dist[i], virginica_dist[i]])), 3)
        nearest_index = np.argmin(np.array([setosa_dist[i], versicolor_dist[i], virginica_dist[i]]))
        print(
            f'A {iris_types[i // 10]} was incorrectly classified as a {iris_types[nearest_index]} (distance of {nearest_dist})')
    # indexes of falsely classified values in original iris_data array
    wrong_indexes = np.concatenate([np.where(wrong_indexes < 10)[0] + 40,
                                    np.where((10 < wrong_indexes) & (wrong_indexes < 20))[0] + 80,
                                    np.where(20 < wrong_indexes)[0] + 120])
    return correct, wrong, wrong_indexes


iris_data = np.empty([150, 4])
# sepal_length, sepal_width,petal_length, petal_width
with open('data.txt', 'r') as f:
    lines = f.readlines()[1:]
    for index in np.arange(len(lines)):
        iris_data[index] = lines[index].split(',')[:4]

# get all test data
test_data = np.concatenate([iris_data[40:50], iris_data[90:100], iris_data[140:]])

# average values per class
averages = np.array([np.mean(iris_data[0:40], axis=0),
                     np.mean(iris_data[50:90], axis=0),
                     np.mean(iris_data[100:140], axis=0)])


def calc_euclidian_distances(averages, test_data):
    # euclidian distances for each test case
    setosa_dist = np.sqrt(np.sum(np.power(test_data - averages[0], 2), axis=1))
    versicolor_dist = np.sqrt(np.sum(np.power(test_data - averages[1], 2), axis=1))
    virginica_dist = np.sqrt(np.sum(np.power(test_data - averages[2], 2), axis=1))
    return [setosa_dist, versicolor_dist, virginica_dist]


print("Euclidian Distance Results: ")
euclidian_distances = calc_euclidian_distances(averages, test_data)
classify(euclidian_distances)


def calc_manhattan_distances(averages, test_data):
    setosa_dist = np.sum(np.fabs(test_data - averages[0]), axis=1)
    versicolor_dist = np.sum(np.fabs(test_data - averages[1]), axis=1)
    virginica_dist = np.sum(np.fabs(test_data - averages[2]), axis=1)
    return [setosa_dist, versicolor_dist, virginica_dist]


print("Manhattan Distance Results: ")
manhattan_distances = calc_manhattan_distances(averages, test_data)
classify(manhattan_distances)


def calc_chebyshev_distances(averages, test_data):
    setosa_dist = np.max(np.fabs(test_data - averages[0]), axis=1)
    versicolor_dist = np.max(np.fabs(test_data - averages[1]), axis=1)
    virginica_dist = np.max(np.fabs(test_data - averages[2]), axis=1)
    return [setosa_dist, versicolor_dist, virginica_dist]


print("Chebyshev Distance Results: ")
chebyshev_distances = calc_chebyshev_distances(averages, test_data)
classify(chebyshev_distances)
