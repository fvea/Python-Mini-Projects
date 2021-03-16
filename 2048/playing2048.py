from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
chrome = webdriver.Chrome(executable_path='..\chromedriver.exe', options=options)
wait = WebDriverWait(chrome, timeout=1)
chrome.get('https://play2048.co/')
htmlElem = chrome.find_element_by_tag_name('html')
keys = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

while True:
    try:
        tryAgainButton = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Try again')))
    except TimeoutException:
        ActionChains(chrome).send_keys_to_element(htmlElem, *keys).perform()
    else:
        print('Game Over!')
        score = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.score-container')))
        print('Your score: {score}'.format(score=score.text))
        break
input()
