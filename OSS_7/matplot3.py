import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal,rand

x = normal(size=1000)
y = normal(size=1000)
plt.scatter(x,y)
plt.show()