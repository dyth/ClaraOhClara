#!/usr/bin/env python
"""create a salt from a theme motif"""
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

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
    return f2(range(x[-1] + 1))


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
positions, theme = convert_known(salt, notesEnum)
theme = interpolate(positions, theme)
print theme
