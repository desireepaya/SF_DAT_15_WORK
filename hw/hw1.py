'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 7/1/2015
'''


import pandas as pd
import seaborn
# pd.set_option('max_colwidth', 50)
# set this if you need to

killings = pd.read_csv('../../SF_DAT_15/hw/data/police-killings.csv')
killings.head()

# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race
killings.rename(columns={'lawenforcementagency':'agency', 'raceethnicity':'race'}, inplace=True)

# 2. Show the count of missing values in each column
killings.isnull().sum()

# 3. replace each null value in the dataframe with the string "Unknown"
killings.streetaddress.fillna(value='Unknown', inplace=True)

# 4. How many killings were there so far in 2015?
killings.count()

# 5. Of all killings, how many were male and how many female?
killings.gender.value_counts()

# 6. How many killings were of unarmed people?
killings[killings.armed == 'No'].armed.value_counts()

# 7. What percentage of all killings were unarmed?
killings[killings.armed == 'No'].armed.value_counts() / killings.armed.count()

# 8. What are the 5 states with the most killings?
killings.state.value_counts().head()

# 9. Show a value counts of deaths for each race
killings.race.value_counts()

# 10. Display a histogram of ages of all killings
killings.hist('age')

# 11. Show 6 histograms of ages by race
killings.age.hist(by=killings.race, sharex=True, sharey=True)

# 12. What is the average age of death by race?
killings.groupby('race').age.mean()

# 13. Show a bar chart with counts of deaths every month
d = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6}
killings['month_no'] = killings['month'].apply(lambda m:d[m])
killings.groupby('month_no').month_no.count().plot(kind='bar')

     
###################
### Less Morbid ###
###################
     
import matplotlib.pyplot as plt
majors = pd.read_csv('../hw/college-majors.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)
del majors['Employed_full_time_year_round']
del majors['Major_code']

# 2. Show the count of missing values in each column
majors.isnull().sum()

# 3. What are the top 10 highest paying majors?
majors[['Major', 'Median']].sort('Median', ascending=False).head(10)

# 4. Plot the data from the last question in a bar chart, include proper title, and labels!
majors[['Major', 'Median']].sort('Median', ascending=False).head(10).plot(x='Major', y='Median', kind='bar', title='Median income by major')

# 5. What is the average median salary for each major category?
major_category_avg = majors.groupby('Major_category').sort('Median', ascending=False).Median.mean()
major_category_avg
# 6. Show only the top 5 paying major categories
major_category_avg[0:5]

# 7. Plot a histogram of the distribution of median salaries
majors.Median.hist()
plt.suptitle('Distribution of median salaries')

# 8. Plot a histogram of the distribution of median salaries by major category
# correction: create a bar chart showing average median salaries for each major_category
major_category_avg.plot(kind='bar', title='Average median salaries per major category')

# 9. What are the top 10 most UNemployed majors?
# What are the unemployment rates?
majors[['Major','Unemployed']].sort('Unemployed', ascending=False).head(10)
majors[['Major', 'Unemployed', 'Unemployment_rate']].sort('Unemployed', ascending=False).head(10)

# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category
# What are the unemployment rates?
majors_cat_unemployed = majors[['Major_category','Unemployed']].groupby('Major_category').mean().sort('Unemployed', ascending=False)
majors_cat_unemployed[0:10]
majors_cat_unemp_rate = majors[['Major_category','Unemployed','Unemployment_rate']].groupby('Major_category').mean().sort('Unemployed', ascending=False)
majors_cat_unemp_rate[0:10]

# 11. The total and employed column refer to the people that were surveyed.
# Create a new column showing the employment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. its 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042
majors['Sample_employment_rate'] = majors['Employed'] / majors['Total']

# 12. Create a "sample_unemployment_rate" column
# this column should be 1 - "sample_employment_rate"
majors['Sample_unemployment_rate'] = 1 - majors['Sample_employment_rate']
