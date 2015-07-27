# -*- coding: utf-8 -*-
"""
Project code for Bitcoin sentiment analysis.

@author: desiree
"""
# import necessary packages
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt

# read in CSV for StockTwits data
stock_twits = pd.read_csv("https://raw.githubusercontent.com/desireesylvester/SF_DAT_15_WORK/master/project/project_data/PS1-BCOIN_ST.csv")
# view the table, there's approximately 4 years of data in the table
stock_twits

# read in CSV for daily BitCoin pricing data
bitcoin_price = pd.read_csv("https://raw.githubusercontent.com/desireesylvester/SF_DAT_15_WORK/master/project/project_data/BAVERAGE-USD.csv")
bitcoin_price

# merge the two dataframes joining on "Date"
merged_data = pd.merge(stock_twits, bitcoin_price, how='inner', on=None, left_on='Date', right_on='Date', left_index=True, right_index=False, sort=True, copy=True)

# verify new dataframe has all columns
merged_data.columns
# rename columns to remove spaces
merged_data.columns = ['date', 'bull_score', 'bear_score', 'bull-bear', 'bull_msg', 'bear_msg', 'total_msg', 'avg_change', 'ask', 'bid', 'last', 'total_vol']

# view a scatterplot feature/response pairs
sns.pairplot(merged_data, x_vars=['bull_score', 'bear_score', 'bull_msg', 'bear_msg'], y_vars='avg_change', size=4.5, aspect=0.7, kind='reg')

# the relationship between number of messages and avg_change seems stronger
# than the bull or bear message intensity

# define features and response
feature_cols = ['bull_msg', 'bear_msg']
X = merged_data[feature_cols]
y = merged_data.avg_change

# create training and testing data sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)

# fit to a logistic regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
zip(feature_cols, logreg.coef_[0])

