#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Must have mcb.bat and mcb.pyw in the same directory.
#  directory must be in Path environment variable.
# Usage: mcb save <keyword> - Saves clipboard to keyword.
#   	 mcb <keyword> - Loads keyword to clipboard.
#    	 mcb list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    # Delete specific clipboard content
    elif sys.argv[1].lower() == 'delete':
        del mcb_shelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
