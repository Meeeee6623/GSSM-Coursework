import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# sepal_length, sepal_width, petal_length, petal_width
iris_data = np.empty([150, 4])
with open('data.txt', 'r') as f:
    lines = f.readlines()[1:]
    for index in np.arange(len(lines)):
        iris_data[index] = lines[index].split(',')[:4]

pca = PCA(n_components=2)
compressed_data = pca.fit_transform(iris_data)

kmeans = KMeans(n_clusters=3)
kmeans.fit(compressed_data)

y_kmeans = kmeans.predict(compressed_data)

true_classes = [[0] * 50, [1] * 50, [2] * 50]
plt.scatter(compressed_data[:, 0], compressed_data[:, 1], c=true_classes, s=50, cmap='viridis',
            labels=['Setosa Data', 'Virginica Data', 'Versicolor Data'])

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5, label='Centroids')

plt.title("Iris Classifications")
plt.legend()

plt.show()
