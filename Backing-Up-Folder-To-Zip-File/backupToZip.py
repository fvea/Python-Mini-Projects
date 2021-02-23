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
    
    # Create the ZIP File.
    print(f'Creating {zipFileName}...')
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames, in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP File.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue    # don't backup the backup ZIP files.
            backupZip.write(os.path.join(foldername, filename), compress_type=zipfile.ZIP_DEFLATED)
    backupZip.close()
    print('Done.')

