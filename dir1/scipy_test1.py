import numpy as np
import scipy.special as sc

out = 0.25j*sc.hankel1(0, k*np.abs(x - y))

out0 = np.linspace(10)

out1 = np.arange(20)
