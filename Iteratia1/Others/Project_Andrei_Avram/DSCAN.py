import pandas as pd
import time
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN

startTime = time.time()

iris_df = pd.read_csv('Reviews.csv')
values = iris_df.iloc[:, [3, 4]].values
dbscan = DBSCAN(eps=0.25, min_samples=10)
model = dbscan.fit(values)

endTime = time.time()

clusterList = list(model.labels_)

print("DBSCAN:")
print("\t Clusters nb: ", len(set(model.labels_)))
print("\t Time:", endTime - startTime)


#file = open("sample.txt", "w")
#for i in range(0, 3):
#    file.write(str(list(values)[i][0]) + "," + str(list(values)[i][1]) + "," + str("color" + str(clusterList[i] + 1)) + "\n")
