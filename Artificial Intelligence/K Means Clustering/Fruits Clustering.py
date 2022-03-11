import keras
import matplotlib.pyplot as plt
import numpy as np
from keras.datasets import mnist
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

(X_train, y_train), (X_test, y_test) = mnist.load_data()

