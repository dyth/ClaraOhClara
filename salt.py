#!/usr/bin/env python
"""create an initial salt from an original string"""
import numpy as np
from scipy.interpolate import interp1d

notes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

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
    
# convert salt into musical notes, wherever possible
salt = "clara"
salt = salt.lower()

theme = ""
for s in salt:
    if s in notes:
        theme += s
    else:
        theme += '_'
        
print theme

# enumerate theme into numbers
themeEnum = [notesEnum[t] for t in theme]

print themeEnum

# calculate gradient and cumulative gradient between notes with real values
themeGrad = []
prev = 0
for itE in themeEnum:
    if itE != 0:
        themeGrad.append(itE - prev)
        prev = itE
    else:
        themeGrad.append(0)
themeGrad = themeGrad[1:]

print themeGrad
# ASK HOW TO DO NUMERICAL INTEGRATION
# KEEP TRACK OF NUMBER OF STEPS, THEN DIVIDE BY THAT VALUE
