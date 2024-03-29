import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score , confusion_matrix
import pickle
import time
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("processed_data.csv")
X = dataset.iloc[:, 1:]
cls = dataset.iloc[:, 0]

X_train, X_test, cls_train, cls_test = train_test_split(X, cls, test_size=0.2, random_state=42)
startTime = time.time()
knn = KNeighborsClassifier(n_neighbors=5,metric='euclidean')

model = knn.fit(X_train, cls_train)

training_time = time.time() - startTime

cls_pred = knn.predict(X_test)
acc = accuracy_score(cls_test, cls_pred)
precision = precision_score(cls_test, cls_pred, average='weighted', zero_division=0)
recall = recall_score(cls_test, cls_pred, average='weighted', zero_division=0)

print("Accuracy = " + str(acc))
print("Training time = " + str(training_time))
print('Precision: %.3f' % precision + ' Recall: %.3f' % recall)

cm = confusion_matrix(cls_test, cls_pred)
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
plt.show()

# with open('./Models/KNN_model.pkl', 'wb') as model_file:
#     pickle.dump(model, model_file)