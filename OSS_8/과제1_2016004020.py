import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from matplotlib.ticker import NullFormatter

plt.clf()

plt.subplot(211)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
y = mu + sigma * np.random.randn(10000)

plt.hist2d(x, y, bins = 40)
plt.show()
plt.grid(True)
