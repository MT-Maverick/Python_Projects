from sklearn.model_selection import train_test_split
from sklearn import datasets, neighbors, metrics 
import pandas as pd
import numpy as np

#we import and load our dataset to the x & y variables:
iris= datasets.load_iris()
X=iris.data
y=iris.target
#we creates a knn object where the k node is 25 and its weight is uniform
knn= neighbors.KNeighborsClassifier(n_neighbors=7, weights='uniform')

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2)

knn.fit(X_train, y_train)

p= knn.predict(X_test)
a= metrics.accuracy_score(y_test, p)

print("predictions",p)
print("accuracy",a)
print("prediction",knn.predict(X))
print("actual:",X)
