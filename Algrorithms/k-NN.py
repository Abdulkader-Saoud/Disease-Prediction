import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# read the dataset 
dataset = pd.read_csv("processed_data.csv")
X = dataset.iloc[:, 1:]
cls = dataset.iloc[:, 0]

# select %20 of dataset for test
# select %80 of dataset to train model
X_train, X_test, cls_train, cls_test = train_test_split(X, cls, test_size=0.2, random_state=42)

# creating instance of KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)       # set k

# train the model
model = knn.fit(X_train, cls_train)

# calculate accuracy
cls_pred = knn.predict(X_test)
acc = accuracy_score(cls_test, cls_pred)

print("Accuracy = " + str(acc))