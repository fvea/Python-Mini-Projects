#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date formats
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with American date format.
datePattern = re.compile(r"""
    ^(.*?)                  # all text before the date.
    ((0|1)?\d)-             # one or two digits for the month.
    ((0|1|2|3)?\d)-         # one or two digits for the day.
    ((19|20)\d\d)           # four digits for the year.
    (.*?)$
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName)

    # Skip files w/o a date
    if mo is None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
