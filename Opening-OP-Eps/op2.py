#! python3
# op.py
#   - Version 2 of op.py 
#   - Opens the web browser to 9anime.to for watching anime One Piece.
#   - Tracks the current episode or can feed cmd arguments for the episode.
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import pyinputplus as pyip
import sys, shelve, os, re

class MyListener(AbstractEventListener):
    def before_quit(self, driver):
        updateNextEps(epsRE.search(driver.current_url).group())
        print('Next episode updated to {nextEps}'.format(nextEps=getEps()))

def main(eps):
    edgeDriver = EventFiringWebDriver(MyEdge(), MyListener())
    edgeDriver.get('https://www12.9anime.to/watch/one-piece.ov8/ep-' + eps)
    pyip.inputYesNo(prompt='Stop Watching? [Y] Yes [N] No')
    edgeDriver.quit()

def updateNextEps(eps):
    '''
        Updates the shelf file with the next episode.
    '''
    with shelve.open(shelfFile) as db:
        db['currentEps'] = str(int(eps) + 1)

def getEps():
    '''
        Returns the current episode stored on the shelf file.
    '''
    with shelve.open(shelfFile) as db:
        currentEps = db['currentEps']
    return currentEps
    
if __name__ == '__main__':
    epsRE = re.compile(r'\d+$')                                             # Pattern for extracting episode number at end of an URL.
    shelfFile = os.path.join(                                               # Shelf file path.
        os.getcwd(),
        r'Python-Mini-Projects\Opening-OP-Eps\currentEps.dat'
    )
    if len(sys.argv) > 1:
        main(eps=sys.argv[1])
    else:
        main(eps=getEps())