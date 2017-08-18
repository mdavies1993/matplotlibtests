#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import modules

label_set = (
        b'Iris-setosa',
        b'Iris-versicolor',
        b'Iris-virginica',
        )


def read_label (label):
    index = -1
    try:
        index = label_set.index(label)
    except:
        print('not found')
    return index 

data = np.loadtxt('bezdekIris.data', delimiter=',', converters={4 : read_label})

A = np.random.normal(5.0,1.5,10000)
B = np.random.normal(5.0,1.5,100)

Y = np.array((A,B))
X = len(Y)
def deviation (mean, value):
    x = math.sqrt((value - mean)**2)
    return x

for i, column in enumerate(Y):
    plt.bar(i, np.mean(column), width = 0.5)
    if len(column) > 150:
        column = modules.compressVals(column)   
    X = modules.markerDistribution(0.5, column, i)  
    plt.plot(X,column, marker='o', markeredgecolor='k', fillstyle='none',
            linestyle='')
plt.title('random data')

plt.show()
