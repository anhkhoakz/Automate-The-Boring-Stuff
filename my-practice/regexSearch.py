#!/usr/bin/env python3
# A program that opens all .txt files in a folder 
# and searches for any line that matches a user-supplied regular expression.
# The results should be printed to the screen.

import os
import re

# Dir Location
print('Enter a directory location: (in which txt files are located)')
direct = input()
os.chdir(direct)

# Regexes
print("Enter the text you'd like to search for: (or a regex)")
givenReg = input()
soloReg = re.compile(givenReg)
lineReg = re.compile(r'^\n.*' + givenReg + r'.*\n$')
txtFileReg = re.compile(r'.*\.txt')

# Texts in Dir
txtFiles = os.listdir(direct)

# Finding line through Regex
for i in range(len(txtFiles)):
    if txtFileReg.search(txtFiles[i]) is not None:
        file = open(txtFiles[i])
        read = file.read()

        outcomeSolo = soloReg.findall(read)
        outcomeLine = lineReg.findall(read)

        print('In ' + txtFiles[i] + ', found these matches:')
        print(outcomeLine)

        print('In ' + txtFiles[i] + ', the lines for these matches were:')
        print(outcomeSolo)

        print('\n')
        file.close()
