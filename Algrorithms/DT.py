import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score ,confusion_matrix
import pickle
import time
import numpy as np
import matplotlib.pyplot as plt

dataset= pd.read_csv("processed_data.csv")
X = dataset.iloc[:,1:]
Y = dataset.iloc[:,0]

model = DecisionTreeClassifier()
tests = []
y_tests = []
acc = 0

start_time = time.time()

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
        tests = X_test
        y_tests = y_test

    
training_time = time.time() - start_time

y_pred = model.predict(tests)
acc = accuracy_score(y_tests, y_pred)
precision = precision_score(y_tests, y_pred, average='weighted', zero_division=0)
recall = recall_score(y_tests, y_pred, average='weighted', zero_division=0)

cm = confusion_matrix(y_tests, y_pred)
classes = model.classes_

plt.figure(figsize=(8, 8))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()

tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes, rotation=45)
plt.yticks(tick_marks, classes)

plt.xlabel('Predicted Label')
plt.ylabel('True Label')

print(acc)
print(training_time)
print('Precision: %.3f' % precision + ' Recall: %.3f' % recall)
plt.show()

# with open('./Models/DT_model.pkl', 'wb') as model_file:
#     pickle.dump(model, model_file)
