import numpy as np


def calc_euclidian(data: np.ndarray):
    s = np.average(np.sqrt(np.power(data[:40, :], 2)))
    ve = np.average(np.sqrt(np.power(data[50:90, :], 2)))
    vi = np.average(np.sqrt(np.power(data[100:140, :], 2)))
    return s, ve, vi


iris_data = np.empty([150, 4])

# "sepal_length","sepal_width","petal_length","petal_width","class"
with open('data.txt', 'r') as f:
    lines = f.readlines()[1:]
    for index in np.arange(len(lines)):
        iris_data[index] = lines[index].split(',')[:4]

print(iris_data)
setosa, versicolor, virginica = calc_euclidian(iris_data)
print(setosa, versicolor, virginica)
