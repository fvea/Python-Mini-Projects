"""
This Python script do the following:

    1. Get the text off the clipboard.
    2. Find all phone numbers and email addresses in the text.
    3. Paste them onto the clipboard.

The script uses Regular Expressions for pattern matching, and
pyperclip module for working with the clipboard.
"""

import re, pyperclip

# Pattern for American phone numbers.
phoneREGEX = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # area code
    (\s|-|\.)?                          # seperator
    (\d{3})                             # first 3 digits
    (\s|-|\.)                           # seperator
    (\d{4})                             # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
)''', re.VERBOSE)

# Pattern for email addresses.
emailREGEX = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   # username
    @                                   # @ symbol
    [a-zA-Z0-9.-]+                      # domain name
    (\.[a-zA-Z]{2,4})                   # dot-something
)''', re.VERBOSE)

# Find matches in the clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneREGEX.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailREGEX.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    matchesFormatted = '\n'.join(matches)
    pyperclip.copy(matchesFormatted)
    print('Copied to the clipboard:')
    print(matchesFormatted)
else:
    print('No phone numbers or email addresses found.')
