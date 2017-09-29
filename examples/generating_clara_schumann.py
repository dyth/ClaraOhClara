#!/usr/bin/env python
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


def interpolate(x, y):
    'interpolate salt from known notes at x'
    if len(x) == 1:
        # if only one point, brute set other points by cypher mentioned above
        brute_salt(x)
    if len(x) == 2:
        # if two points, linearly interpolate
        f2 = interp1d(x, y, kind='linear')
    if len(x) == 3:
        # if three points, quadratically interpolate
        f2 = interp1d(x, y, kind='quadratic')
    else:
        # otherwise do cubic interpolation
        f2 = interp1d(x, y, kind='cubic')
    return f2

x = [0.0, 2.0, 4.0]
y = [3.0, 1.0, 1.0]

f = interp1d(x, y)
f2 = interpolate(x, y)

xnew = np.linspace(0.0, 4.0, num=40)
xtune = range(int(x[-1]) + 1)

plt.plot(
    x, y, 'o',
    xnew, f(xnew), '-',
    xnew, f2(xnew), '--',
    xtune, f2(xtune), '-'
)
plt.legend(['data', 'linear', 'cubic', 'tune'], loc='best')
plt.show()
