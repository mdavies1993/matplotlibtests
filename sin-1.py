import math
import matplotlib.pyplot as plt 

T=range(100)
x=[(2*math.pi*t)/len(T) for t in T]
y=[math.sin(value) for value in x]

plt.plot(x,y)
plt.show()
