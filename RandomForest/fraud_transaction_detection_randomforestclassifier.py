# -*- coding: utf-8 -*-
"""Fraud Transaction Detection-RandomForestClassifier

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12IE6wjVqM0Rtor2XDka3exO1SXCjYMfr
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_excel("transaction.xlsx")
data = data.drop('Transaction ID', axis=1)
data= data.drop('Time of Transaction', axis=1)
# Convert categorical variables to numerical using one-hot encoding
data = pd.get_dummies(data, columns=['Unusual Action'], drop_first=True)

scaler = StandardScaler()
data['Transaction Amount'] = scaler.fit_transform(data[['Transaction Amount']])
data

x = data.drop('Fraudulent', axis=1)
y = data['Fraudulent']

X_train, X_test, Y_train, Y_test= train_test_split(x, y, test_size=0.2, random_state=42)

RF = RandomForestClassifier()
RF.fit(X_train, Y_train)

pred = RF.predict(X_test)
print(pred)

print("Accuracy: ", accuracy_score(Y_test, pred))
print("Classification Report: ", classification_report(Y_test, pred))

New = pd.DataFrame({
    'Transaction Amount': [900, 505, 555, 1000, 400],
    'Unusual Action':['No', 'Yes', 'No', 'No', 'Yes']
})

New = pd.get_dummies(New, columns=['Unusual Action'], drop_first=True)
New['Transaction Amount'] = scaler.transform(New[['Transaction Amount']])

new = RF.predict(New)
print(new)