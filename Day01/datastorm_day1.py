# -*- coding: utf-8 -*-
"""DataStorm Day1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bXu0yD_7XvMYh_GNsh0gWPK31cE_lGAg
"""

!git clone https://github.com/Sadeesha-Sath/DataStorm.git

!ls

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import seaborn as sns
import warnings

ori_dataset = pd.read_csv('./DataStorm/train_data.csv')
dataset = ori_dataset.copy()
dataset['ItemCode'] = dataset['ItemCode'].map(str)
dataset.head()

dataset['DateID'] = dataset["DateID"].map(lambda x: dt.datetime.strptime(x, "%m/%d/%Y").weekday())
dataset.rename(columns={'DateID': 'DayOfWeek'}, inplace=True)

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

len(x)

len(y)

dataset

x[1]

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

print(x[1])

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x[:, 4:] = sc.fit_transform(x[:, 4:])

x

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x, y)

dataset