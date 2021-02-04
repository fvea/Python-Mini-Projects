#! python3
# dateDetection.py 
#   - detects dates in DD/MM/YYYY format in a given text.

# TODO: DATE REGEX
#   Create regular expression for the dates in DD/MM/YYYY format.
#   Assume that days, months and years range from 01-31, 01-12, and
#   1000-2999 respectively.

import re

dateREGEX = re.compile(r'''(
    ((0[1-9])|([1-2]\d)|(3[0-1]))   # day 01-31
    (/|-)                           # seperator
    ((0[1-9])|(1[0-2]))             # month 01-12 
    (/|-)                           # seperator
    ([1-2]\d{3})                    # year 1000-2999 
)''', re.VERBOSE)




# TODO:
#   Fetch month, day and year from detected date.
#   Check if the date is valid, if yes add it to the 
#   list of detected dates. 

# TODO:
#   Print the dates found, or print a message if no dates are found.

