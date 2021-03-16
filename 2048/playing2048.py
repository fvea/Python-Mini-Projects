from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def play2048(*keyCombinations):
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    chrome = webdriver.Chrome(executable_path='..\chromedriver.exe', options=options)
    chrome.get('https://play2048.co/')
    # chrome.maximize_window()
    htmlElem = chrome.find_element_by_tag_name('html')
    print("Computer's playing...")
    while True:
        try:
            chrome.find_element(By.LINK_TEXT, 'Try again')
        except NoSuchElementException:
            ActionChains(chrome).send_keys_to_element(htmlElem, *keyCombinations).perform()
        else:
            print('Game Over!')
            score = chrome.find_element(By.CSS_SELECTOR, 'div.score-container')
            print("Computer's score: {score}".format(score=score.text))
            break
    input()

if __name__ == '__main__':
    keyCombinations = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]
    play2048(*keyCombinations)