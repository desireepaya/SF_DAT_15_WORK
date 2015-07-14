# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:00:03 2015
Evaluation of ZYX Corp (SPY - S&P500 index)
@author: desiree
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../data/ZYX_prices.csv')
data.head()
data.info()

# this didn't do what I expected, I was trying to calculate average sentiment per tweet.  Need to revisit
ZYX_10min_avg = data['ZYX10minSentiment'] / ['data.ZYX10minTweets']

sns.lmplot(x=data.ZYX10minSentiment, y= data.ZYX10minPriceChange, data=data, ci=None)

plt.scatter(data.ZYX5minSentiment, data.ZYX30minPriceChange)

ZYX10min_bool = np.where(data.ZYX10minPriceChange > 0, 1, 0)

plt.plot(data.ZYX10minSentiment, ZYX10min_bool, color='red')

linreg = LinearRegression()
feature_cols = ['ZYX5minSentiment']
X = data[feature_cols]
y = data['ZYX30minPriceChange']
linreg.fit(X, y)

print linreg.intercept_
print linreg.coef_

linreg.score(X,y)
ZYX5min_pred = linreg.predict(X)

plt.scatter(data.ZYX5minSentiment, data.ZYX30minPriceChange)
plt.plot(data.ZYX5minSentiment, ZYX5min_pred, color='red')

sns.pairplot(data, x_vars=['list'], y_vars='predictor', size=4.5, aspect=0.7, kind='reg')


