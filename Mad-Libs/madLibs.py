#! python3
# madLibs.py - Reads text files and lets the user add their own
# text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears
# in the text file.


# LOGIC:
#   1. Create Regex for ADJECTIVE, NOUN, ADVERB or VERB.
#   2. Open target text file/s, and search for all occurence of the Regex object.
#   3. Prompt the user for replacing words.
#   4. Replace the matched regex with replacing word/s, save it as new content.
#   5. Write the new content to new file.

import re
import sys
from pathlib import Path

# Location of target file.
filePath = Path.cwd() / 'Mad-Libs'

# Create Regex pattern for ADJECTIVE, NOUN, ADVERB, or VERB
REGEX = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

# Read the content of the text file and 
# find all the occurrence of the Regex pattern.
with open(filePath / 'sample.txt', 'r') as fileObj:
    content = fileObj.read()
    matches = REGEX.findall(content)

if len(matches) == 0:
    print('No matches(ADJECTIVE, NOUN, ADVERB or VERB) found.')
    sys.exit()

# Prompt the user for replacing words.
replacingWords = []
for found in matches:
    print('Enter an %s:' % (found.lower()))
    replacingWords.append(input())

# Replace the found patterns by new ones.
newContent = content
for word in replacingWords:
    newContent = REGEX.sub(word, newContent, count=1)

print('\nOld Content:\n' + content + '\n')
print('New Content:\n' + newContent + '\n')

# Write the modified content to a new file.
with open(filePath / 'sample_replaced.txt', 'w') as fileObj:
    fileObj.write(newContent)

print('New content written to: sample_replaced.txt')











