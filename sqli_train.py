import pandas as pd
import matplotlib.pyplot as plt
from joblib import dump
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix, ConfusionMatrixDisplay

# load dataset
data = pd.read_csv('Datasets/Modified_SQL_Dataset.csv')

# Define feature extractor
vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')

# feature extraction
X = vectorizer.fit_transform(data['Query'])
y = data['Label']

# Divide training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a support vector machine classifier
clf = SVC(kernel='linear', random_state=42)

# training model
clf.fit(X_train, y_train)

# prediction test set
y_pred = clf.predict(X_test)

# Calculate model performance metrics
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

# output performance index
print("##### Model Performance ####")
print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Recall: {:.2f}%".format(recall * 100))
print("Precision: {:.2f}%".format(precision * 100))
print("F1-score: {:.2f}%".format(f1 * 100))
print("Specificity: {:.2f}%".format(tn / (tn + fp) * 100))
print("Sensitivity: {:.2f}%".format(tp / (tp + fn) * 100))

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=clf.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.show()

# Save the model and vectoriser object
dump(clf, 'web_app/hospital/sqli_ml/model.joblib')
dump(vectorizer, 'web_app/hospital/sqli_ml/vectorizer.joblib')