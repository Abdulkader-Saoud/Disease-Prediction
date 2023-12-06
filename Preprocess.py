import pandas as pd
from sklearn.preprocessing import  LabelEncoder
from sklearn.model_selection import train_test_split ,RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt


data = pd.read_csv('dataset.csv')
disease_label_encoder = LabelEncoder()
disease_encoded = disease_label_encoder.fit_transform(data['Disease'])
encoded_disease_mapping = dict(zip(disease_label_encoder.classes_, range(len(disease_label_encoder.classes_))))



df = pd.concat([pd.DataFrame({'Disease': disease_encoded}), pd.get_dummies(data.iloc[:, 1:], prefix='', prefix_sep='')], axis=1)

df.to_csv('encoded_data.csv', index=False)

#Decision Tree Classifier

X = df.drop(columns=['Disease'])
y = df['Disease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(max_depth=50, min_samples_split=2, random_state=42)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy: " + str(accuracy))


fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(clf, 
                   feature_names= df.columns[1:],  
                   class_names=  list(encoded_disease_mapping.keys()),
                   filled=True)

plt.savefig('DecisionTree.pdf')
