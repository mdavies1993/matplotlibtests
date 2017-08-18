#!/usr/bin/python3
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as fctk
from matplotlib.backends.backend_tkagg import FigureManagerTkAgg as fmtk
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy as sp
import pandas as pd

class Setup():
    def __init__(self):
        self.master = Tk()
        self.fig = mpl.figure.Figure(figsize=(6,5),dpi=100)
        self.canvas = fctk(self.fig,master = self.master)
        self.fig_manager = fmtk(self.canvas,0,self.master)
        self.fig_manager.show()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        #self.master.after(200,self.draw)
        #self.canvas.show()
        #self.canvas.get_tk_widget().pack(side=TOP,fill=BOTH,expand=1)
    def ax(self):
        return self.fig.add_subplot(111)
    def draw(self):
        self.fig.canvas.draw()

    def on_closing(self):
        self.master.quit()
        self.master.destroy()
    def reset(self):
        
        self.canvas = Fc(self.fig,master=self.master)
        self.canvas.get_tk_widget().grid(row=0,column=0,columnspan=4)

