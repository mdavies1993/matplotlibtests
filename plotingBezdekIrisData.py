#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import modules
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as fc
from tkinter import *

fig = plt.figure()
ax = fig.add_subplot(111)

data = pd.read_csv('bezdekIris.data',header=None)
grouped = data.groupby(4)

ax.set_xlim(.5,len(grouped)+1)

colIndexDict = {}
i = 0
errorbars = []
for name, group in grouped:
    colIndexDict[name] = i
    i += 1
    gap = .8/(group.shape[1]-1)
    x = (np.arange(group.shape[1]-1)*gap)+i
    mean = group.mean()
    sem = group.sem()
    ax.bar(x,mean.as_matrix(),width=gap,color=['r','g','b','k'])
    for j in range(len(x)):
        xmarkers, ymarkers = modules.markerDistribution(x[j],group[j].as_matrix(),gap,
                )
        plt.plot(xmarkers, ymarkers, alpha=.1, 
                marker='o', markeredgecolor='k', fillstyle='none',linestyle='')

    errbar = ax.errorbar(x,mean.as_matrix(),yerr=sem,linestyle='none',capsize=7, 
            ecolor='k')
    errorbars.append(errbar)

    
master = Tk()
canvas = fc(fig,master=master)
canvas.get_tk_widget().grid(row=0,column=0,columnspan=4)

def on_closing():
    master.quit()

master.protocol("WM_DELETE_WINDOW", on_closing)
master.mainloop()
