import warnings
# Suppress warnings from skopt using deprecated sklearn API
warnings.filterwarnings('ignore', category=FutureWarning,
                        message='sklearn.externals.joblib is deprecated')
warnings.filterwarnings('ignore', category=FutureWarning,
                        message='the sklearn.metrics.scorer module')

import pandas as pd  
# reading csv file 
data = pd.read_csv('iris.csv') 
# shape of dataset 
print("Shape:", data.shape) 
# column names 
#print("\nFeatures:", data.columns) 
# storing the feature matrix (X) and response vector (y) 
X = data[data.columns[:-1]] 
y = data[data.columns[-1]] 
# printing first 5 rows of feature matrix 
print("\nFeature matrix:\n", X.head()) 
# printing first 5 values of response vector 
#print("\nResponse vector:\n",y.head())
  
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(X)

'''
https://towardsdatascience.com/machine-learning-algorithms-part-9-k-means-example-in-python-f2ad05ed5203
'''
import matplotlib.pyplot as plt
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
