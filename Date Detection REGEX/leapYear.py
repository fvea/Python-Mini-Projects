#! python3
# leapYear.py
#   - contains isleapYear(year) function that checks
#     wether the given year is leap year or not.

def isleapYear(year):
    ''' Returns True if the year is leap year. '''
    intYear = int(year)

    if intYear % 4 == 0 and not (intYear % 100 == 0 and intYear % 400 != 0):
        return True
    return False