#! python3
# cmd_email2.py
#       - Version 2 of the cmd_emailer.py
#       - A command line emailer.
#       - Takes an email address and string of text on the command line.
#       - Sends an email of the string to the provided address.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, time

def sendOutlookEmail(recipient, message):
    '''
        Sends an email with a content <message> to <recipient>.
    '''
    # Create an instance of the MS Edge Webdriver.
    edgeDriver = webdriver.Edge()
    edgeDriver.get('https://outlook.live.com/mail/')
    edgeDriver.maximize_window()

    try:
        # Do sign in.
        signInButton = WebDriverWait(edgeDriver, timeout=10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Sign in'))
        )
        signInButton.click()

        # Click new message button.
        newMsgButton = WebDriverWait(edgeDriver, timeout=10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.root-40 > button > span'))
        )
        newMsgButton.click()

        # Compose the email.
        edgeDriver.implicitly_wait(10)
        toField = edgeDriver.find_element_by_css_selector('input[aria-label="To"]')
        toField.send_keys(recipient)
        subject = "You've got a new message from {sender}".format(sender='fjvinceatabay@outlook.com')
        subjectField = edgeDriver.find_element_by_css_selector('input[aria-label="Add a subject"]')
        subjectField.send_keys(subject)
        msgBody = edgeDriver.find_element_by_css_selector('div[aria-label="Message body"]')
        msgBody.send_keys(message)
        sendButton = edgeDriver.find_element_by_css_selector('button[aria-label="Send"]')
        sendButton.click()
    except Exception as exc:
        print('An error has occured: {exc}'.format(exc=exc))
        print('Could not send the email to {recipient}'.format(recipient=recipient))
    else:
        print('Email Sent!')
        time.sleep(10)
        edgeDriver.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sendOutlookEmail(recipient=sys.argv[1], message=' '.join(sys.argv[2:]))
    else:
        print('No cmd arguments given.')




