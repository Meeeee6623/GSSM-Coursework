import numpy as np


def test_training(distances: list, euclid_data: np.ndarray):
    # grab all test values
    test_data = np.concatenate([euclid_data[40:50], euclid_data[90:100], euclid_data[140:]])
    # get distances to each type, for each testing value
    setosa_dist = np.fabs(test_data - distances[0])
    versicolor_dist = np.fabs(test_data - distances[1])
    virginica_dist = np.fabs(test_data - distances[2])

    # boolean array of correct vs. false classifications
    classifications = np.concatenate([setosa_dist[0:10] < np.minimum(versicolor_dist[0:10], virginica_dist[0:10]),
                                      versicolor_dist[10:20] < np.minimum(setosa_dist[10:20], virginica_dist[10:20]),
                                      virginica_dist[20:] < np.minimum(versicolor_dist[20:], setosa_dist[20:])])

    correct = np.count_nonzero(classifications)
    wrongnum = len(test_data) - correct
    wrongval = np.where(~classifications)[0]
    # indexes of falsely classified values in original euclid_data array
    wrongval = np.concatenate([np.where(wrongval < 10)[0] + 40,
                               np.where((10 < wrongval) & (wrongval < 20))[0] + 80,
                               np.where(20 < wrongval)[0] + 120])
    return correct, wrongnum, wrongval


def calc_euclidian(data: np.ndarray):
    # all values with euclidian mean
    euclid_data = np.sqrt(np.sum(np.power(data, 2), axis=1))
    # mean per flower type
    s = np.mean(euclid_data[0:40])
    ve = np.mean(euclid_data[50:90])
    vi = np.mean(euclid_data[100:140])
    return np.array([s, ve, vi]), euclid_data


iris_data = np.empty([150, 4])
# sepal_length, sepal_width,petal_length, petal_width
with open('data.txt', 'r') as f:
    lines = f.readlines()[1:]
    for index in np.arange(len(lines)):
        iris_data[index] = lines[index].split(',')[:4]

distances, euclid_data = calc_euclidian(iris_data)
right, wrong, wrong_indexes = test_training(distances, euclid_data)
print(f'{right} Irises were correctly classified.')
print(f'{wrong} Irises were incorrectly classified:')
for i in wrong_indexes:
    iris_types = ['setosa', 'versicolor', 'virginica']
    nearest_dist = np.round(np.amin(np.fabs(euclid_data[i] - distances)), 3)
    nearest_index = np.argmin(np.fabs(euclid_data[i] - distances)) - 1
    print(f'A {iris_types[i // 40 - 1]} was incorrectly classified as a {iris_types[nearest_index]} (distance of {nearest_dist})')
