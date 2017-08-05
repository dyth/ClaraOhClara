#!/usr/bin/env python
"""create an initial salt from an original string"""

notes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

notesEncoding = {
    'a' : 'a',
    'b' : 'b',
    'c' : 'c',
    'd' : 'd',
    'e' : 'e',
    'f' : 'f',
    'g' : 'g',
    
    'h' : 'a',
    'i' : 'b',
    'j' : 'c',
    'k' : 'd',
    'l' : 'e',
    'm' : 'f',
    'n' : 'g',
    
    'o' : 'a',
    'p' : 'b',
    'q' : 'c',
    'r' : 'd',
    's' : 'e',
    't' : 'f',
    'u' : 'g',
    
    'v' : 'a',
    'w' : 'b',
    'x' : 'c',
    'y' : 'd',
    'z' : 'e'
}

# convert salt into 
salt = "clara"
salt = salt.lower()

theme = ""
for s in salt:
    theme += notesEncoding[s]
print theme
