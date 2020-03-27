import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# reading csv file 
data = pd.read_csv('iris.csv') 
# shape of dataset 
print("Shape:", data.shape) 
# column names 
#print("\nFeatures:", data.columns) 
# storing the feature matrix (X) and response vector (y) 
X = data[data.columns[:-1]] 
y = data[data.columns[-1]]

#print("\nFeature matrix:\n", X.head())

'''
https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py
'''

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

db = DBSCAN(eps=1.3, min_samples=5).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
if n_clusters_ >1 :
    print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))
