import numpy as np

def test(distances: list, euclid_data: np.ndarray):
  test_data = np.concatenate(euclid_data[40:50], euclid_data[90:100], euclid_data[140:])
  print(test_data)
  setosa_dist = np.fabs(test_data - distances[0])
  versicolor_dist = np.fabs(test_data - distances[0])
  virginica_dist = np.fabs(test_data - distances[0])

  correct = np.sum(
    np.count_nonzero(test_data[0:10] -  
    setosa_dist[0:10] < np.min(versicolor_dist[0:10], virginica_dist[0:10])),
    np.count_nonzero(test_data[10:20] -  
    versicolor_dist[10:20] < np.min(setosa_dist[10:20], virginica_dist[10:20])),
    np.count_nonzero(test_data[20:] -  
    setosa_dist[20:] < np.min(versicolor_dist[20:], virginica_dist[20:]))
    )
  wrong = len(test_data) - correct
  return correct, wrong


def calc_euclidian(data: np.ndarray):
    euclid_data = np.sqrt(np.sum(np.power(data, 2), axis=1))
    s = euclid_data[0:40]
    ve = euclid_data[50:90]
    vi = euclid_data[100:140]
    return s, ve, vi, euclid_data


iris_data = np.empty([150, 4])

# "sepal_length","sepal_width","petal_length","petal_width","class"
with open('data.txt', 'r') as f:
    lines = f.readlines()[1:]
    for index in np.arange(len(lines)):
        iris_data[index] = lines[index].split(',')[:4]

# print(iris_data)
setosa, versicolor, virginica, euclid_data = calc_euclidian(iris_data)
print(euclid_data)
print(test([setosa, versicolor, virginica], euclid_data))
