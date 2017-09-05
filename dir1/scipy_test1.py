import numpy as np
import scipy.special as sc

out = 0.25j*sc.hankel1(0, k*np.abs(x - y))
