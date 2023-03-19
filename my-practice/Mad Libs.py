#! /usr/bin/env python3

import re, shelve

madFile = shelve.open('Mad Libs.txt',)
text = input('Please type your text:\n')
madFile['text'] = text
madFile.close()

regex = re.compile(r'ADJECTIVE|NOUN|VERB|NOUN')
matches = regex.findall(text)

for word in matches:
    user_input = input('Enter %s: ' %word)
    text = text.replace(word,user_input,1)

print(text)