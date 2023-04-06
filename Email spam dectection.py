# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MZuZeUdaq3o67cICj71C7WDtxmUN6nGD
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV

email = pd.read_csv("spam.csv",encoding ='ISO-8859-1')
email

email = email.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1)
email = email.dropna()
email.info()

X = email['v2'].values
y = email['v1'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
X_test = cv.transform(X_test)

from sklearn.svm import SVC
svm = SVC(kernel = 'rbf', random_state=0)
svm.fit(X_train,y_train)

y_pred = svm.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy*100)