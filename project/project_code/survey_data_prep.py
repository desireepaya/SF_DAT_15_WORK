# -*- coding: utf-8 -*-
"""
@author: desireesylvester
The following actions are completed in this script:
- read in a collection of excel files
- merge files into one large dataframe
- modify columns to for analysis
- save new dataframe as a csv
"""

import pandas as pd
# read in surveys excel worksheets
jan15 = pd.read_excel('C:/Users/desiree/Dropbox/GIT/SF_DAT_15_WORK/project/project_data/011915.xls', sheetname=2)
feb15 =  pd.read_excel('C:/Users/desiree/Dropbox/GIT/SF_DAT_15_WORK/project/project_data/021915.xls', sheetname=2)
mar15 = pd.read_excel('C:/Users/desiree/Dropbox/GIT/SF_DAT_15_WORK/project/project_data/031915.xls', sheetname=2)
apr15 = pd.read_excel('C:/Users/desiree/Dropbox/GIT/SF_DAT_15_WORK/project/project_data/041915.xls', sheetname=2)
sep14 = pd.read_excel('C:/Users/desiree/Dropbox/GIT/SF_DAT_15_WORK/project/project_data/091914.xls', sheetname=2)
oct14 = pd.read_excel('C:/Users/desiree/Dropbox/GIT/SF_DAT_15_WORK/project/project_data/101914.xls', sheetname=2)
nov14 = pd.read_excel('C:/Users/desiree/Dropbox/GIT/SF_DAT_15_WORK/project/project_data/111914.xls', sheetname=2)
# merge all new dataframes into single df called survey_merged
survey_merged = sep14.append(oct14, ignore_index=True)
survey_merged = survey_merged.append(nov14, ignore_index=True)
survey_merged = survey_merged.append(jan15, ignore_index=True)
survey_merged = survey_merged.append(feb15, ignore_index=True)
survey_merged = survey_merged.append(mar15, ignore_index=True)
survey_merged = survey_merged.append(apr15, ignore_index=True)

# Data preparation
# remove response time columns
survey_merged.drop(survey_merged.columns[30:40], axis=1, inplace=True)
# evaluate usefulness of different columns, ex: Parental Status
survey_merged['Parental Status'].value_counts()
"""
Unknown       7613
Non-parent     288
Parent          39
Most of the data is 'Unknown', so drop the column
"""
# remove User ID, Publisher Category, Geography, Parental Status, Weight
survey_merged.drop(['User ID','Publisher Category','Geography','Parental Status', 'Weight'], axis=1, inplace=True)
# remove multiple choice responses for questions 7 and 8
survey_merged.drop(survey_merged.columns[11:23], axis=1, inplace=True)
# rename remaining columns
survey_merged.columns = ['date','gender','age','city_type','income','familiarity','use_frequency','trust_scale','useful_now','useful_future','top_of_mind','legal_fraud_scale','regulate_ban_scale']
# update field for 'date' that takes just the date portion of the data
survey_merged['date'] = survey_merged['date'].str[:10]
# save updated dataframe for later use
survey_merged.to_csv('project_data/survey_clean.csv', index=False)