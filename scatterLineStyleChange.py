#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def pdf(X, mu, sigma):
    a = 1.0/(sigma*np.sqrt(2.0*np.pi))
    b = -1.0/(2.0*sigma**2)
    return a * np.exp(b * (X-mu) ** 2)

X = np.linspace(-6,6,2400)

plt.plot(X, pdf(X, 0.0,1.0), color = 'k',linestyle='solid')
plt.plot(X, pdf(X, 0.0,0.5), color = 'k',linestyle='dashed')
plt.plot(X, pdf(X, 0.0,0.25), color = 'k',linestyle='dashdot')
plt.show()
