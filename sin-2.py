import numpy as np 
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi, 100)
ya=np.sin(x)
yb=np.cos(x)

plt.plot(x,ya)
plt.plot(x,yb)
plt.show()

