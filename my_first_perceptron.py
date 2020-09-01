# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

# loading iris dataset
import os
import pandas as pd
s = os.path.join('https://archive.ics.uci.edu', 'ml', 
                 'machine-learning-databases',
                 'iris', 'iris.data')

df = pd.read_csv(s,
                 header=None,
                 encoding='utf-8')

print(df.tail())

# prepare data
import matplotlib.pyplot as plt
import numpy as np

# select setosa and versicolor
Y = df.iloc[0:100, 4].values 
Y = np.where(Y == 'Iris-setosa', -1, 1)

# extract sepal length and petal length
X = df.iloc[0:100, [0, 2]].values

# plot data 
plt.scatter(X[:50, 0], X[:50, 1],
            color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='blue', marker='x', label='versicolor')
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()