# -*- coding: utf-8 -*-
"""housing price prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K4ksvulruDSNXu_KOe9c8C0i-Ea18tHg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor

from google.colab import files

uploaded= files.upload()

df1=pd.read_excel("house (2).xlsx")

paru=df1

paru.head()

paru.describe()

paru.isnull().sum()

paru.dropna()

paru.drop_duplicates(inplace = True)

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Area")
sns.distplot(paru['Area'])
plt.show()

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Price_in_ lakh")
sns.distplot(paru['Price'])
plt.show()

correlation = paru.corr()
print(correlation["Area"].sort_values(ascending=False))

predict = "Price"
data = paru[[ "Price","Area","Bedroom"]]
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(xtrain, ytrain)
predictions = model.predict(xtest)

from sklearn.metrics import mean_absolute_error
model.score(xtest, predictions)

X = paru[["Area","Bedroom"]]

y = paru['Price']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=None)

from sklearn.linear_model import LinearRegression

linreg = LinearRegression()
linreg.fit(X_train, y_train)

print (linreg.intercept_)
print (linreg.coef_)

Price = linreg.intercept_+4.28493975*55+5.34103721*20

print("the Price is ",Price, "lakh for a area of 55 sqr mtr and 20 Bedrooms")

"""The model pridict that for a  Area = 55 sqr mtr and number of bedroom =20  the price will be of 328.97 lakh"""

Price = linreg.intercept_+4.28493975*50+5.34103721*18

print("the Price is ",Price1, "lakh for a area of 50 sqr mtr and 18 Bedrooms")

model_efficiency = ((Price1/300)*100)

print(model_efficiency)

"""the model pridict that for a area of 50 sqr mtr and 18 Bedrroms the price is293.0137 lakh and as per data the price should be 300 lakh for same parameter so model efficiency is 97.671 %"""