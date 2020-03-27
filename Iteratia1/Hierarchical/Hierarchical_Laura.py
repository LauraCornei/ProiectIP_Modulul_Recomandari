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

from sklearn.cluster import AgglomerativeClustering

cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
cluster.fit_predict(X)

print(cluster.labels_)


'''
https://www.geeksforgeeks.org/implementing-agglomerative-clustering-using-sklearn/
determinare nr maxim de clustere
din dendoagram - cea mai mare distanta intre intersectiile cu o linie orizontala
din silhouette_score - cea mai mare valoare
'''
import scipy.cluster.hierarchy as shc
plt.figure(figsize=(10, 10))
plt.title("Dendograms")
dend = shc.dendrogram(shc.linkage(X, method='ward'))
plt.show()

#------------------------------

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
k = [2, 3, 4, 5, 6, 7] 
ac0 = AgglomerativeClustering(n_clusters = k[0],affinity='euclidean', linkage='ward')
ac1 = AgglomerativeClustering(n_clusters = k[1],affinity='euclidean', linkage='ward')
ac2 = AgglomerativeClustering(n_clusters = k[2],affinity='euclidean', linkage='ward')
ac3 = AgglomerativeClustering(n_clusters = k[3],affinity='euclidean', linkage='ward')
ac4 = AgglomerativeClustering(n_clusters = k[4],affinity='euclidean', linkage='ward')
ac5 = AgglomerativeClustering(n_clusters = k[5],affinity='euclidean', linkage='ward')
# Appending the silhouette scores of the different models to the list 
score = [] 
score.append( 
        silhouette_score(X, ac0.fit_predict(X))) 
score.append( 
        silhouette_score(X, ac1.fit_predict(X))) 
score.append( 
        silhouette_score(X, ac2.fit_predict(X))) 
score.append( 
        silhouette_score(X, ac3.fit_predict(X))) 
score.append( 
        silhouette_score(X, ac4.fit_predict(X))) 
score.append( 
        silhouette_score(X, ac4.fit_predict(X)))  
# Plotting a bar graph to compare the results 
plt.bar(k, score) 
plt.xlabel('Number of clusters', fontsize = 20) 
plt.ylabel('S(i)', fontsize = 20) 
plt.show() 
