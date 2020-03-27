import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

dataset = pd.read_csv('./iris.csv')

dataColumns = [0, 1, 2, 3]
clustersNr = 3

x = dataset.iloc[:, dataColumns].values
print(type(dataset.iloc))
kmeans = KMeans(n_clusters=clustersNr).fit(x)

plt.scatter(x[:, 0], x[:, 1],c=kmeans.predict(x), cmap='rainbow')
plt.show()
