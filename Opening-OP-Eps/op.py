#! python3
# op.py
#   - Opens the web browser to 9anime.to for watching anime One Piece.
#   - Tracks the current episode or can feed cmd arguments for the episode.
import os, sys, shelve, webbrowser

URL = 'https://www13.9anime.to/watch/one-piece.ov8/ep-'
shelfPath = os.path.join(os.getcwd(), r'Python-Mini-Projects\Opening-OP-Eps')
shelfFileName = 'currentEps'

def updateShelfFile(eps):
    eps = str(int(eps) + 1)
    with shelve.open(os.path.join(shelfPath, shelfFileName)) as db:
        db['currentEps'] = eps

def getEps():
    with shelve.open(os.path.join(shelfPath, shelfFileName)) as db:
        currentEps = db['currentEps']
    return currentEps

def main():
    if len(sys.argv) > 1:
        eps = ' '.join(sys.argv[1:])
        del sys.argv[1:]
    else:
        eps = getEps()
    updateShelfFile(eps)
    
    nextEpsURL = URL + eps
    print('Opening {}'.format(nextEpsURL))
    webbrowser.open(nextEpsURL)

if __name__ == '__main__':
    ans = ''
    while(ans != 'n'):
        main()
        ans = input('Jump to next eps?[y] Yes [n] No: ')





