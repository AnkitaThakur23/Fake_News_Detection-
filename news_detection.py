-# -*- coding: utf-8 -*-
"""Fake_News_Detection

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lPuh5grwN80zNuWM-m1URIwKq_m51pMo
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

data = pd.read_csv("fake_or_real_news.csv")

data['fake'] = data['label'].apply(lambda x: 0 if x == "REAL" else 1)

data = data.drop("label", axis=1)

X, y = data["text"], data["fake"]

x_train, x_test,y_train= train_test_split(X,y,test_size=0.2)

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
x_train_vectorized = vectorizer.fit_transform(x_train)
x_test_vectorized = vectorizer.transform(x_test)

clf = LinearSVC()
clf.fit(x_train_vectorized, y_train)

clf.score(x_test_vectorized, y_test)

len(y_test)

with open("mytext.txt", "w" , endoding ="utf-8") as f:
    f.write(x_test.iloc[10])

with open("mytext.txt", "r", encoding="utf-8") as f:
    text = f.read()

vectorized_text = vectorizer .transfrom([text])

clf.predict(vectorized_text)

y_test.iloc[10]





