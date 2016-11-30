import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal,rand

a = np.random.randint(100,size = 1000)
plt.hist(a,bins=100)
plt.show()
plt.cla()