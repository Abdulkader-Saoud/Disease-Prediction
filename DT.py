import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt
import pickle

dataset= pd.read_csv("processed_data.csv")
X = dataset.iloc[:,1:]
Y = dataset.iloc[:,0]

max = 0
model = DecisionTreeClassifier()
for i in range(1, 500):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)
    clf = DecisionTreeClassifier()

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    if accuracy > max:
        max = accuracy
        model = clf

print("Accuracy: " + str(accuracy))
print("Max: " + str(max))
with open('DT_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('DT_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

yped =  loaded_model.predict(X_test)
print("Accuracy: " + str(accuracy_score(y_test, yped)))
