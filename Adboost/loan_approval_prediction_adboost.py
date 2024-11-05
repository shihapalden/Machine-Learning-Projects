# -*- coding: utf-8 -*-
"""Loan-Approval-Prediction-Adboost

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17q37QbV0hN7CFHIe-FgneLr344l7C2yw
"""

import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('Loan-Approval-Prediction.csv').drop(['Loan_ID', 'Gender', 'Married', 'Property_Area', 'Dependents'], axis=1)

education_map = {'Graduate': 1, 'Not Graduate': 0}
self_employed_map = {'Yes': 1, 'No': 0}
loan_status_map = {'Y': 1, 'N': 0}

data['Education'] = data['Education'].map(education_map)
data['Self_Employed'] = data['Self_Employed'].map(self_employed_map)
data['Loan_Status'] = data['Loan_Status'].map(loan_status_map)
data = data.dropna()

x = data.drop('Loan_Status', axis=1)
y = data['Loan_Status']

X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.2, random_state=42)

model = AdaBoostClassifier()
model.fit(X_train, Y_train)

pred = model.predict(X_test)
print("Accuracy: ", accuracy_score(Y_test, pred))

new_data = pd.DataFrame({
    'Education': [education_map['Graduate']],
    'Self_Employed': [self_employed_map['No']],
    'ApplicantIncome': [5000],
    'CoapplicantIncome': [0],
    'LoanAmount': [128],
    'Loan_Amount_Term': [360],
    'Credit_History': [1]
})

prediction = model.predict(new_data)
print("Loan Approval Prediction:", 'Approved' if prediction[0] == 1 else 'Not Approved')