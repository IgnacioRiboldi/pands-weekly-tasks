# Plot Task
# This program generates two different plots.
# By Ignacio Riboldi

import numpy as np 
import matplotlib.pyplot as plt

x = np.random.normal(5, 2, 1000)

plt.title('Weekly Task - Histogram')
plt.xlabel('Values')
plt.ylabel('Mean')

plt.hist(x) 
plt.show() 

x = np.linspace(0, 10, 500)
h_x = x**3

plt.figure(figsize=(8, 6))
plt.plot(x, h_x, color='b', label=r'$h(x) = x^3$', linewidth=2)


plt.title('Weekly Task - Plot')
plt.xlabel('x')
plt.ylabel('h(x)')


plt.legend()

plt.show() 
plt.savefig('plot.png')