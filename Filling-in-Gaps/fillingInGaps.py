#! python3
# fillinInGaps.py - program that finds all files with a given prefix, 
# such as spam001.txt, spam002.txt, and so on, in a single folder and 
# locates any gaps in the numbering (such as if there is a spam001.txt 
# and spam003.txt but no spam002.txt). The program renameS all the later 
# files to close this gap.

# Logic:
#   1. Create Regex pattern for spam00x.txt
#   2. Set the starting number, which is 1.
#   3. Loop through the files in the given folder.
#   4. if the current filename matched the Regex:
#       4.1 fetch the number part
#       4.2 if the number part is the not the same with 
#           the current starting number, break
#   5. Loop trough the files in the given folder.
#   6. if the current filename matched the Regex:
#       6.1 fetch the number part
#       6.2 if the number part is greater than the starting number:
#           6.2.1 copy the current file to other location and rename it with the current starting number.
#       6.3 else copy the current file to other location.

import os, re, shutil

REGEX = re.compile(r'''
    ^(spam)              # the prefix spam
    (0{,2})              # zero to two intances of 0's
    (\d+)                # number-part
    (.txt)               # extension-part
    $
    ''', re.VERBOSE)

def fillInGaps(folder):
    '''
    Fill in's missing gaps in numbered text file names.
    '''
    folder = os.path.abspath(folder)
    filenames = os.listdir(folder)
    print(filenames)
    number = 1
    for filename in filenames:
        mo = REGEX.search(filename)
        if mo is None:
            continue
        numberPart = int(mo.group(3))
        print(numberPart)
        if numberPart > number:
            newFileName = mo.group(1) + mo.group(2) + str(number) + mo.group(4)
            print(f'Renaming {filename} to {newFileName}')
            shutil.copy(os.path.join(folder, filename), os.path.join(os.getcwd(), newFileName))
        else:
            shutil.copy(os.path.join(folder, filename), os.getcwd())
        number = number + 1

if __name__ == '__main__':
    folder = r'C:\Users\fvea\Documents'
    fillInGaps(folder)




