from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

iris = load_iris()
X = iris.data
Y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names
print(feature_names[0], feature_names[2])
# attributes = X[:, (0, 2)]

#dendrograma
# dendrogram = sch.dendrogram(sch.linkage(X, method='average'))
# plt.show()

colors = ["b", "g", "r", "y", "m", "c"]
model = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='average')
model.fit(X)
labels = model.labels_
attributes = X[:, (0, 2)]
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[2])
for i in range(len(attributes)):
    plt.scatter(attributes[i][0], attributes[i][1], color=colors[labels[i]])
plt.show()
print("all good")
