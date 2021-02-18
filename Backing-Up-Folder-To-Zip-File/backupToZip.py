#! python3
# backupToZip.py - Copies an entire folder and its contents
# into a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)    # Make sure folder is absolute.

    # Figure out the filename this code should use based on
    # what files already existing on.
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1