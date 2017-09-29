#!/usr/bin/env python
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from math import ceil, floor
from decimal import Decimal


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


def nearest_upper_note(x):
    'if note is an integer, then it is not interpolated, do not edit'
    if abs(x - int(x)) < 0.00000000000001:
        return float(int(x))
    else:
        return 0.5*ceil(2.0*x)


def nearest_lower_note(x):
    'if note is an integer, then it is not interpolated, do not edit'
    if abs(x - int(x)) < 0.00000000000001:
        return float(int(x))
    else:
        return 0.5*floor(2.0*x)


x = [0.0, 2.0, 4.0]
y = [3.0, 1.0, 1.0]

f = interp1d(x, y)
f2 = interpolate(x, y)

xnew = np.linspace(0.0, 4.0, num=40)
xtune = range(int(x[-1]) + 1)
tune = f2(xtune)

floors = [nearest_lower_note(t) for t in tune]
ceilings = [nearest_upper_note(t) for t in tune]

print tune
print [2.0*t for t in tune]
print "ceilings", ceilings
print "floors", floors

plt.plot(
    x, y, 'o',
    xnew, f2(xnew), '--',
    xtune, tune, '-',
    xtune, ceilings, '-',
    xtune, floors, '-'
)
plt.legend(['data', 'interpolation', 'tune', 'ceiling', 'floor'], loc='best')
plt.savefig('clara.png', dpi=200)
plt.show()
