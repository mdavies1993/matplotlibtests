import matplotlib.pyplot as plt 
x = range(100)
y = [value ** 2 for value in x]
print(x)
print(y)

plt.plot(x, y)
plt.show()
