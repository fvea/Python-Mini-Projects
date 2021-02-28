#! python3
# mapIt.py - gets a street address from command line args
# or clipboard and opens the web browser for the Google Maps
# page for the address.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from the clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)