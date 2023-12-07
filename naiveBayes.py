import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# read the dataset 
dataset= pd.read_csv("encoded_data.csv")
X = dataset.iloc[:,1:]
cls = dataset.iloc[:,0]
# selects %20 of dataset for test
# selects %80 for training model
X_train, X_test, cls_train, cls_test = train_test_split(X, cls, test_size=0.2, random_state=42)
# creating instance of NB
NB = BernoulliNB()
# train the model
model = NB.fit(X_train, cls_train)
# calculate accuracy
cls_pred = NB.predict(X_test)
acc = accuracy_score(cls_test,cls_pred)

print("Accuracy = " + str(acc))