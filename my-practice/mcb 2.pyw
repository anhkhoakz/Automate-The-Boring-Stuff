#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:    py.exe mcb.pyw save <keyword> - saves clipboard to keyword.
#           py.exe mcb.pyw <keyword> - loads keyword to clipboard
#           py.exe mcb.pyw list - loads all keywords to clipboard
#           py.exe mcb.pyw clr - clears all keywords and clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
# TODO: save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'clr':
        if sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]


elif len(sys.argv) == 2:
    # list keywords and load content.
    if sys.argv[1].lower() == 'clr':
        mcbShelf.clear()
    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[mcbShelf[sys.argv[1]]])

mcbShelf.close()
