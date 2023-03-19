'''
Extending the Multi-Clipboard
Extend the multi-clipboard program in this chapter so that it has a delete 
<keyword> command line argument that will delete a keyword from the shelf. 
Then add a delete command line argument that will delete all keywords.
'''
#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - delete keyword.
#        py.exe mcb.pyw delete - delete all content.

import shelve, pyperclip, sys
from pathlib import Path

(Path.cwd() / 'mcb').mkdir(exist_ok=True)
mcbShelf = shelve.open('MCB/mcb')

if len(sys.argv) == 3:
    # Save clipboard content.
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # Delete <keyword>.
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # Delete all content.
    if sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    # List keywords and load content.
    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    
      
mcbShelf.close()