#!/usr/bin/env python
"""create a salt from a theme motif"""

def convert_known(salt):
    'from salt, convert all known notes'
    salt = salt.lower()

    theme, positions = [], []
    for s in salt:
        if s in notes:
            theme.append(s)
    theme = [notesEnum[t] for t in theme]
    return theme, positions


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
        f2 = = interp1d(x, y, kind='cubic')
    return f2(range(x[-1] + 1))
