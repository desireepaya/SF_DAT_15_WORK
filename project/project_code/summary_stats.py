# -*- coding: utf-8 -*-
"""
@author: desireesylvester
This code performs the following actions:
-
"""
import pandas as pd

survey = pd.read_csv('project_data/survey_clean.csv')

#explore data
survey['familiarity'].value_counts()
survey['age'].value_counts()
survey['gender'].value_counts()
survey['city_type'].value_counts()
# remove 'top_of_mind' column, it's evaluated in another script
survey.drop('top_of_mind', axis=1, inplace=True)
# remove any row where data='Unknown'
survey = survey[survey.gender != 'Unknown']
survey = survey[survey.age != 'Unknown']
survey = survey[survey.city_type != 'Unknown']
# graph scalar responses
survey.hist(by='gender', bins=5)
survey.hist(by='age', bins=5)
survey.hist(by='city_type', bins=5)






