#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

N = 8
A = np.random.random(N)
B = np.random.random(N)
X = np.arange(N)

lw, ec = 2.0, 'k'

plt.bar(X, A, color = '0.75',linewidth =lw, edgecolor = ec)
plt.bar(X, A+B, bottom = A, color = 'w', linewidth = lw, edgecolor = ec, linestyle = 'dashed')

plt.show()
