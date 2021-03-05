#! python3
# rjt.py - uses requests module to download a copy of
# whole Romeo and Juliet play from the hard-coded link
# below.

import requests
from pathlib import Path

rjt_link = 'https://automatetheboringstuff.com/files/rj.txt'
res = requests.get(rjt_link)               # Get a response object for the request from server.
try:
    res.raise_for_status()
except Exception as exc:                   # Crashes the program if there's an error from the request.
    print(f'There was a problem: {exc}')
else:
    # Write the downloaded text file to hard drive.
    playFile = Path.cwd() / 'RomeoAndJuliet.txt'
    with open(playFile, 'wb', encoding='utf-8') as fObj:
        for chunk in res.iter_content(100000):
            fObj.write(chunk)
