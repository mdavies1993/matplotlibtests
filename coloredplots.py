#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def pdf(X, mu, sigma):
    a = 1.0/(sigma*np.sqrt(2.0*np.pi))
    b = -1.0/(2.0*sigma**2)
    return a * np.exp(b * (X-mu) ** 2)

X = np.linspace(-6,6,1000)

for i in range(5):
    samples = np.random.standard_normal(50)
    mu, sigma = np.mean(samples), np.std(samples)
    plt.plot(X, pdf(X, mu, sigma), color = '.75')
    print(pdf(X,mu,sigma))

plt.plot(X, pdf(X, 0.0, 1.0), color='k')
plt.show()
