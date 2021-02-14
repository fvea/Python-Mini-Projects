#! python3
# regexSearch.py - Opens all .txt files in a folder and searches for any
# line that matches a user-supplied regular expression.

# LOGIC:
#   1. Prompt the user for the regular expression.
#   2. Compile the given regular expression.
#   3. If there's a problem in compilation, exit the program.
#   4. Create a WindowsPath object for the target directory of .txt files.
#   5. Fetch all the files w/ .txt extension.
#   6. Loop through all the files and look for the regex matches.
#   7. Save the matches in dictionary with keys as the filename and values as the matches.
#   8. Print the results.

import re
import pprint
from pathlib import Path

# Prompt the user for regular expression, and compile it.
print('Enter a valid regular expression:')
REGEX = re.compile(r'%s' % input())

# Create a WindowsPath object for the target directory of .txt files.
targetDir = Path.cwd() / 'Regex-Search'

# Create a list of text files from the target directory.
textFiles = targetDir.glob('*.txt')

# Look for patterns in the text files.
results = {}
for textFile in textFiles:
    with open(textFile, 'r') as fileObj:
        matches = REGEX.findall(fileObj.read())
        if len(matches) > 0:
            results[textFile.name] = matches

# Print results
pprint.pprint(results)





