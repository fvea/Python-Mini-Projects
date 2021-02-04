#! python3
# dateDetection.py 
#   - detects dates in DD/MM/YYYY format in a given text.

import re
from leapYear import isleapYear

dateREGEX = re.compile(r'''(
    (0[1-9]|[1-2]\d|3[0-1])   # day 01-31
    (/|-)                           # seperator
    (0[1-9]|1[0-2])             # month 01-12 
    (/|-)                           # seperator
    ([1-2]\d{3})                    # year 1000-2999 
)''', re.VERBOSE)

text = input()
matches = []
for date in dateREGEX.findall(text):
    day, month, year = date[1], date[3], date[5]        # fetch day, month, and year
    maxDays = 31
    if month in ('04', '06', '09', '11'):               # 04, 06, 09 and 11 are months w/ 30 days.
        maxDays = 30
    elif month == '02':
        if isleapYear(year):
            maxDays = 29
        else: 
            maxDays = 28
    if int(day) <= maxDays:
        matches.append('/'.join([day, month, year]))


if len(matches) > 0:
    print('Found Dates:')
    print('\n'.join(matches))
else:
    print('No DD/MM/YYYY date format found.')

