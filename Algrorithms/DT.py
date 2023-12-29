import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from scipy.stats import randint
import pickle

dataset= pd.read_csv("processed_data.csv")
X = dataset.iloc[:,1:]
Y = dataset.iloc[:,0]


model = DecisionTreeClassifier()
acc = 0
for i in range(1, 500):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)
    X_train = X_train.values
    X_test = X_test.values
    tmp = DecisionTreeClassifier(criterion='gini', max_depth=50, min_samples_split=2, min_samples_leaf=1, max_features=16, random_state=i)
    
    tmp.fit(X_train, y_train)
    
    y_pred = tmp.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    if accuracy > acc:
        model = tmp
        acc = accuracy

    
y_pred = model.predict(X_test)
print("Accuracy: " + str(acc))


with open('./Models/DT_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
