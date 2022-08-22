import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import math
mean = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(-3, 3, 201)
plt.plot(x, norm.pdf((x-mean)/sigma),linewidth=2.0, label='normal PDF')
plt.plot(x, norm.cdf((x-mean)/sigma),linewidth=2.0, label='normal CDF')
plt.legend(bbox_to_anchor=(.35,1))
plt.show()