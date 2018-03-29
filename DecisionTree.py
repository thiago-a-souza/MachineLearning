'''
AUTHOR:
 Thiago Alexandre Domingues de Souza

LANGUAGE:
 Python3

INPUT:
 The input file has both training set and test set. The first row has the attribute names (e.g. outlook, temperature, humidity and wind) and the class name (play). The following lines represents the training set, stored as string values. The last line describe the test evaluated.

SAMPLE INPUT:
 outlook,temperature,humidity,wind,play
 sunny,hot,high,weak,no
 sunny,hot,high,strong,no
 ...
 sunny,cool,high,strong,
'''

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

data = pd.read_csv('input/play_tennis.csv')

# get_dummies is used to convert categorical data (e.g. sunny, rainy, etc) into numeric values
train_features = pd.get_dummies(data[['outlook','temperature','humidity','wind']])

# Initial rows represent the training set
training = train_features[:-1]
# Last row is test set
testing = train_features[-1:]

# LabelEncoder is used to convert class labels to numeric values
le = LabelEncoder()
labels = le.fit_transform(data['play'][:-1])

# DecisionTreeClassifier supports two partitioning schemes: entropy (a.k.a information gain) and gini
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(training, labels)

result = clf.predict(testing)

print("Output: ", le.inverse_transform(result))

