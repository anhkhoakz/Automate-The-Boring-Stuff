#! /usr/bin/env python3
# bulletPointAdder.py - Adds Wikipedia bullet poins
# to the start of each line of text on clipboard

import pyperclip
text = pyperclip.paste()
print(text)

#TODO: Seperate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i]='* ' + lines[i]
text = '\n'.join(lines)
print('\nWorking:')
print(text)

pyperclip.copy(text)

#Lists of animals
#Lists of aquarium life
#Lists of biologists by author abbreviation
#Lists of cultivars
