#!/usr/bin/python3
from setupTk import Setup
import numpy as np 
import matplotlib as mpl
import pandas as pd
import modules as mods

dataInPath = './biotin_conc_tht.csv'

def onSave(figureToSave):
    figureToSave.savefig(dataInPath[:-3]+'png',dpi=600)
def main():
    fig_master = Setup(onSave)
    ax = fig_master.ax()

    raw_data = pd.read_csv(dataInPath,skiprows=6,header=None).values[:,2:]
    x = raw_data[0,1:]/(60**2)
    y = raw_data[1:,:]
    y,keys = mods.group_data(y)
    labels = np.loadtxt('biotin_conc_tht_labels.txt',dtype='str')
    for label in labels:
        print(label)
    icol = 0
    scatterplts = []
    smplsize = np.linspace(0,1,len(keys)-3)
    colors=[]
    for col in smplsize:
        colors.append((1-col,0,0))
    for col in range(len(keys)-len(smplsize)):
        colors.append('C'+str(int(col)))
    for group in y:
        scplt = ax.plot(np.transpose(x),group,marker='o',markeredgecolor=colors[icol],ls='', ms=2.5,fillstyle='none',label=labels[icol])
        for i in range(len(scplt)):
            if i != 2:
                scplt[i].set_label('_none_')
        scatterplts.append(scplt)
        icol +=1
    ax.set_xlim(np.amin(x),np.amax(x))
    legend = ax.legend()
    legend._loc = 1
    legend.set_bbox_to_anchor((1,0.6))
    ax.set_xlabel(r'$Time\ (hrs)$')
    ax.set_ylabel(r'Flourescence 560\textit{nm} (au)')
    fig_master.draw()
    fig_master.master.mainloop()

if __name__=='__main__':main()
