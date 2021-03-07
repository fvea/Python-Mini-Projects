#! python3
# op.py
#   - Opens the web browser to 9anime.to for watching anime One Piece.
#   - Tracks the current episode or can feed cmd arguments for the episode.
import os, sys, shelve, webbrowser

URL = 'https://www13.9anime.to/watch/one-piece.ov8/ep-'
shelfPath = os.path.join(os.getcwd(), r'Python-Mini-Projects\Opening-OP-Eps')
shelfFileName = 'currentEps'

def updateShelfFile(eps):
    '''
        Updates the shelf file with the next episode.
    '''
    eps = str(int(eps) + 1)
    with shelve.open(os.path.join(shelfPath, shelfFileName)) as db:
        db['currentEps'] = eps

def getEps():
    '''
        Returns the current episode stored on the shelf file.
    '''
    with shelve.open(os.path.join(shelfPath, shelfFileName)) as db:
        currentEps = db['currentEps']
    return currentEps

def main():
    if len(sys.argv) > 1:
        eps = sys.argv[1]
        del sys.argv[1:]
    else:
        eps = getEps()

    epsURL = URL + eps
    print('Opening {}...'.format(epsURL))
    webbrowser.open(epsURL)
    print("You're currently watching episode-{}...".format(eps))
    updateShelfFile(eps)
    print('Next episode updated to: {}'.format(getEps()))

if __name__ == '__main__':
    main()





