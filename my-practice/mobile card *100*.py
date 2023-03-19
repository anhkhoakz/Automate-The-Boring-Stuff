#! /usr/bin/env python3
# bulletPointAdder.py - Adds *100*...# on mobile card
# to the start and end of each line of text on clipboard

import pyperclip
text = pyperclip.paste()

#TODO: Seperate lines and add *100*...#.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i]='*100*' + lines[i]+'#'
text = '\n'.join(lines)

pyperclip.copy(text)
