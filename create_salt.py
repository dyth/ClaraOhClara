#!/usr/bin/env python
"""create a salt from a theme motif"""
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from math import ceil, floor


notes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def convert_known(salt, notesEnum):
    'from salt, convert all known notes'
    salt = salt.lower()
    theme, positions = [], []
    for i in range(len(salt)):
        if salt[i] in notes:
            positions.append(i)
            theme.append(notesEnum[salt[i]])
    return positions, theme


def interpolate(x, y):
    'interpolate salt from known notes at x'
    # if only one point, brute set other points by cypher mentioned above
    # if two points, linearly interpolate
    # if three points, quadratically interpolate
    # otherwise do cubic interpolation
    if len(x) == 1:
        brute_salt(x)
    if len(x) == 2:
        f2 = interp1d(x, y, kind='linear')
    if len(x) == 3:
        f2 = interp1d(x, y, kind='quadratic')
    else:
        f2 = interp1d(x, y, kind='cubic')
    return f2(range(x[-1] + 1))


def nearest_upper_note(x):
    'if note within representational error, it is not interpolated,\
    do not edit otherwise take upper 0.5'
    if abs(x - int(x)) < 0.00000000000001:
        return float(int(x))
    else:
        return 0.5*ceil(2.0*x)


def nearest_lower_note(x):
    'if note within representational error, it is not interpolated,\
    do not edit otherwise take lower 0.5'
    if abs(x - int(x)) < 0.00000000000001:
        return float(int(x))
    else:
        return 0.5*floor(2.0*x)

    
def create_theme_bounding_package(salt, notesEnum):
    'create a bounding region for each note'
    positions, theme = convert_known(salt, notesEnum)
    theme = interpolate(positions, theme)
    floors = [nearest_lower_note(t) for t in theme]
    ceilings = [nearest_upper_note(t) for t in theme]
    return floors, ceilings


notesEnum = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    '_': 0
}

    
salt = "Clara"
floors, ceilings = create_theme_bounding_package(salt, notesEnum)

print floors
print ceilings
