import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal,rand
  
t = np.arange(0.0, 10.0 , 0.01)
s = np.sin(2*np.pi*t)
c = np.cos(2*np.pi*t)
plt.plot(t,s)
plt.plot(t,c)
plt.show()
plt.cla()

