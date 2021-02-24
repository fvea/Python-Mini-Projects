#!python3
# unneededFiles.py - program that walks through a folder tree 
# and searches for exceptionally large files or folders—say, ones 
# that have a file size of more than 100MB.

# Logic:
#   1. create function named unneededFiles(path).
#   2. walk through the given path.
#   3. check if current file in list of filenames in the current
#       folder has a size greater than 100MB, if yes, print it.

import os

def unneededFiles(path):
    """
    Walks the folder in the given path, and prints
    all the files with the file size greater than 100MB.
    """
    path = os.path.abspath(path)    # Make sure the path is absolute.

    for folderName, subfolders, fileNames in os.walk(path):
        for filename in fileNames:
            filepath = os.path.join(path, folderName, filename)
            fileSize = os.path.getsize(filepath)
            if fileSize > 100e6:
                print(f'{filepath} has size {fileSize}bytes.')
    print('DONE.')

if __name__ == '__main__':
    samplePath = r'C:\Users\fvea\Downloads'
    unneededFiles(samplePath)
