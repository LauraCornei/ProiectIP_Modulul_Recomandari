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
#print("\nFeature matrix:\n", X.head()) 
# printing first 5 values of response vector 
#print("\nResponse vector:\n",y.head())
  
# splitting X and y into training and testing sets 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1) 

# training the model on training set
from sklearn import neighbors
#from neighbors import neighborsKNeighborsClassifier
knn = neighbors.KNeighborsClassifier(n_neighbors=3,weights='uniform',algorithm='kd_tree',p=1) 
knn.fit(X_train, y_train) 
  
# making predictions on the testing set 
y_pred = knn.predict(X_test) 
  
# comparing actual response values (y_test) with predicted response values (y_pred) 
from sklearn import metrics 
print("kNN model accuracy:", metrics.accuracy_score(y_test, y_pred)) 
  
# making prediction for out of sample data 
sample = [[3, 5, 4, 2], [2, 3, 5, 4]] 
preds = knn.predict(sample) 

print("Predictions:", preds) 
  
# saving the model 
from sklearn.externals import joblib 
joblib.dump(knn, 'iris_knn.pkl')

