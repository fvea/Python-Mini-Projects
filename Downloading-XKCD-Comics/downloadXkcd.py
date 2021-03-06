#! python3
#  downloadXkcd.py - Downloads every single XKCD comic.

import requests, bs4, os

url = 'https://xkcd.com/'               # starting url.
os.makedirs('xkcd', exist_ok=True)      # store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % (url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print("Couldn't find the image.")
    else:
        comicURL = 'http:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicURL))
        res = requests.get(comicURL)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imgFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
        for chunk in res.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()
    
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('DONE.')


        
         

