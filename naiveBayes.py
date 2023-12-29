import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


dataset= pd.read_csv("processed_data.csv")
X = dataset.iloc[:,1:]
Y = dataset.iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

NB = BernoulliNB()

model = NB.fit(X_train, y_train)

cls_pred = NB.predict(X_test)
acc = accuracy_score(y_test,cls_pred)

print("Accuracy = " + str(acc))