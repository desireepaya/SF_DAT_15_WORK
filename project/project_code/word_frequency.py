# -*- coding: utf-8 -*-
"""
@author: desireesylvester
The following actions are completed in this script:
- data preparation for frequency analysis
- analyze frequency of words
"""
import pandas as pd
survey = pd.read_csv('project_data/survey_clean.csv')

"""
Natural Language Processing
Evaluate words associated with BitCoin provided by respondents
"""
import nltk
nltk.download()
from collections import Counter

# create a new dataframe for word association responses for BitCoin
words = survey.top_of_mind
# count word frequency
c_words = Counter(words)
c_words.most_common(25)
"""
Returns an interesting list of terms:
[('scam', 431),
 ('money', 301),
 ('fraud', 214),
 ('nothing', 121),
 ('internet', 96),
 ('digital currency', 77),
 ('coin', 76),
 ('fake money', 71),
 ('none', 65),
 ("don't know", 54),
 ('risky', 52),
 ('internet money', 50),
 ('no', 48),
 ('currency', 47),
 ('fad', 47),
 ('fake', 46),
 ('not sure', 40),
 ('idk', 40),
 ('bitcoin', 38),
 ('shady', 38),
 ('doge', 35),
 ('gold coin', 34),
 ('black market', 33),
 ('virtual currency', 33),
 ('coins', 32)]
 Could reducing each token to its stem provide a better view?
"""
# use stemming to consolidate words with the same root
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
# stem our tokens
stemmed_tokens = [stemmer.stem(w) for w in words]
# count the stemmed tokens
c = Counter(stemmed_tokens)
c.most_common(25)
"""
[(u'scam', 434),
 (u'money', 301),
 (u'fraud', 214),
 (u'noth', 121),
 (u'coin', 108),
 (u'internet', 96),
 (u'digital curr', 77),
 (u'fake money', 71),
 (u'none', 65),
 (u"don't know", 54),
 (u'riski', 52),
 (u'internet money', 50),
 ('no', 48),
 (u'currenc', 47),
 (u'fad', 47),
 (u'fake', 46),
 (u'hacker', 43),
 (u'bitcoin', 40),
 (u'gold coin', 40),
 (u'idk', 40),
 (u'not sur', 40),
 (u'shadi', 38),
 (u'comput', 37),
 (u'anonym', 37),
 (u'drug', 36)]
 We see a slight increase in tops terms, but no real change.
 """