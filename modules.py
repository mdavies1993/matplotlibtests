import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby
#set the x values to plot the markers 
#the markers imitate a histogram with the width 
#giving a normalised frequency 
def markerDistribution (xVal, yVals, width, maxsize=100):
    if len(yVals) > maxsize:
        yVals = compressVals(yVals, maxsize)
    xVals = np.full(len(yVals),xVal)
    bins = np.linspace(np.amin(yVals),np.amax(yVals),np.sqrt(len(yVals)))
    inds = np.digitize(yVals,bins)-1
    bincount = np.bincount(inds)
    counter = 0
    maxBcnt = np.amax(bincount)
    minBcnt = np.amin(bincount)
    binWidths = np.full((2,len(bins)),None)
    for i in range(binWidths.shape[1]):
        #column 0  = the start/current width 
        #column 1 = the increment size 
        bcntwidth = ((bincount[i]-minBcnt)/(maxBcnt - minBcnt))*width
        binWidths[0,i] = -(bcntwidth/2)
        if bincount[i] > 1:
            binWidths[1,i] = bcntwidth/(bincount[i]-1)
        else:
            binWidths[1,i] = 0.0
    for i in range(len(xVals)):
        xVals[i] = binWidths[0,inds[i]]+xVals[i] #add x to place over correct bar
        binWidths[0,inds[i]] += binWidths[1,inds[i]]
    return xVals, yVals

def compressVals (vals,maxsize):
    compressSize = len(vals)//maxsize
    vals = vals[compressSize::compressSize]
    return vals
def group_data(values):
    grouped_data = []
    uniquekey = []
    for k,g in groupby(values,lambda values:values[0]):
        group = []
        for item in g:
            group.append(item)
        grouped_data.append(np.transpose(np.array(group)[:,1:]))
        uniquekey.append(k)
    return grouped_data, uniquekey
