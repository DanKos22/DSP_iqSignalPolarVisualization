# -*- coding: utf-8 -*-
"""
@author: Dan Koskiranta
"""

import numpy as np
import matplotlib.pyplot as plt


# In-phase/real part
i = np.array([0.5, 0.5, -0.5, -0.5])
# Quadrature/imaginary part
q = np.array([-0.25, 0.25, -0.25, 0.25])
# IQ signal = i+1j*q
iq = i + 1j*q
# Print, with label
print('IQ', iq)
# Calc theta, th
theta = np.arctan2(q, i) 
# Calc magnitude, r
r = np.abs(iq)
# Print, with labels
print('theta', theta)
print('r', r)

# Polar plot IQ signal
fig = plt.figure(figsize=(14,10))
ax = fig.add_subplot(111, projection='polar')
ax.plot(theta, r, '.', markersize=20)
ax.set_rmax(2)
ax.set_rticks([0, 1, 2])
ax.tick_params(axis='both', which='major', labelsize=20)
ax.spines['polar'].set_visible(False)
plt.show()