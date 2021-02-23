#! python3
# selectiveCopy.py - walks through a folder tree and searches for files with
# a certain file extension(.txt) and copies these files from whatever location
# they are into a new folder.


# LOGIC:
#   1. import shutil for copying folder mechanism.
#   2. import os for path handling.
#   3. create function selectiveCopy()
#   4. walk to the given path folder.
#   5. if the current filename in current folder ends with .txt extension, copy it to destination folder.

import os, shutil

def selectiveCopy(folder, destinationFolder):
    """
    Copies files with the .txt extension in a given path folder 
    to given destination folder.
    """
    # Make sure each folder is absolute.
    folder = os.path.abspath(folder)
    destinationFolder = os.path.abspath(destinationFolder)

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.txt'):
                print(f"""Copying {os.path.join(foldername, filename)}
                    to {os.path.join(destinationFolder, filename)}...""")
                shutil.copy(folder, destinationFolder)
    
    print('DONE.')

if __name__ == '__main__':
    from pathlib import Path
    path = Path.home()
    selectiveCopy(path / 'some_folder', path / 'some_folder_copy')

