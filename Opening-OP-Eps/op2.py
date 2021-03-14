#! python3
# op.py
#   - Version 2 of op.py 
#   - Opens the web browser to 9anime.to for watching anime One Piece.
#   - Tracks the current episode or can feed cmd arguments for the episode.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import sys, shelve, os, re

epsRE = re.compile(r'\d+$')
URL = 'https://www12.9anime.to/watch/one-piece.ov8/ep-'
shelfPath = os.path.join(os.getcwd(), r'Python-Mini-Projects\Opening-OP-Eps')
shelfFileName = 'currentEps'

class MyListener(AbstractEventListener):
    def before_close(self, driver):
        updateNextEps(epsRE.search(driver.current_url).group())
        print('Next episode updated to {nextEps}'.format(nextEps=getEps()))

def updateNextEps(eps):
    '''
        Updates the shelf file with the next episode.
    '''
    with shelve.open(os.path.join(shelfPath, shelfFileName)) as db:
        db['currentEps'] = str(int(eps) + 1)

def getEps():
    '''
        Returns the current episode stored on the shelf file.
    '''
    with shelve.open(os.path.join(shelfPath, shelfFileName)) as db:
        currentEps = db['currentEps']
    return currentEps

def main(eps):
    edgeDriver = EventFiringWebDriver(webdriver.Edge(), MyListener())
    edgeDriver.get(URL + eps)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(eps=sys.argv[1])
    else:
        main(eps=getEps())