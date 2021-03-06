#! python3
# searchpypi.py - Opens several search results on pypi.org

import bs4, requests, webbrowser, sys

print('Searching...')            # Display text while downloading the search result page.
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urtToOpen = 'https://pypi.org/' + linkElems[i].get('href')
    print('Opening', urtToOpen)
    webbrowser.open(urtToOpen)
