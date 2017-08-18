#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
data = np.array([[5.,25.,50.,20.],[4.,23.,51.,17.],[6.,22.,52.,19.]])

color_list=['b','g','r']
gap = .8/len(data)
for i, row in enumerate(data):
    X = np.arange(len(row))
    plt.bar(X + i*gap,row,width=gap,color=color_list[i%len(color_list)])
    
plt.show()
