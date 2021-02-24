#! python3
# fillinInGaps.py - program that finds all files with a given prefix, 
# such as spam001.txt, spam002.txt, and so on, in a single folder and 
# locates any gaps in the numbering (such as if there is a spam001.txt 
# and spam003.txt but no spam002.txt). The program renameS all the later 
# files to close this gap.

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
    folder = os.path.abspath(folder)                # Make sure the path is absolute.
    filenames = os.listdir(folder)
    print(filenames)
    number = 1                                      # Starting number.
    for filename in filenames:
        mo = REGEX.search(filename)
        if mo is None:                              # Ignore files that is not a match to default filename.
            continue
        numberPart = int(mo.group(3))
        print(numberPart)
        if numberPart > number:                     # Rename files with their number part greater than the current number.
            newFileName = mo.group(1) + mo.group(2) + str(number) + mo.group(4)
            print(f'Renaming {filename} to {newFileName}')
            shutil.copy(os.path.join(folder, filename), os.path.join(os.getcwd(), newFileName))
        else:
            shutil.copy(os.path.join(folder, filename), os.getcwd())
        number = number + 1

if __name__ == '__main__':
    folder = r'C:\Users\fvea\Documents'
    fillInGaps(folder)




