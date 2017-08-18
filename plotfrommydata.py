#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('my_data.txt')
for column in data.T:
    plt.plot(data[:,0],column)

plt.show()
