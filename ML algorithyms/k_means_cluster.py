from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import scale
import pandas as pd

#load data:
bc =load_breast_cancer()
X=scale(bc.data)
y=bc.target

#create testing & training data:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#creates the k_means model & fits it:
model=KMeans(n_clusters=2, random_state=0)
model.fit(X_train)

#generates the prediction variable:
predictions=model.predict(X_test)

#anaysis of preformance:
lables=model.labels_
print('lable:',lables)
print('accuracy:',accuracy_score(y_test,predictions))
print('prediction:',predictions)
print('actual:',y_test)

print(pd.crosstab(y_train,lables))
