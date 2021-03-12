#! python3
# cmd_email.py 
#   - A command line emailer.
#   - Takes an email address and string of text on the command line.
#   - Sends an email of the string to the provided address.

from selenium import webdriver
import sys, time

if not len(sys.argv) > 1:
    print('Error. Please Input Command Line Arguments.')
    print('Input example: username@email.com Hello, World')
    sys.exit()

# Create the browser object.
edgeBrowser = webdriver.Edge()
edgeBrowser.get('https://outlook.live.com/mail/')       # Open the browser to outlook website.
#time.sleep(2)

# Sign-in to my default account.
signInButton = edgeBrowser.find_element_by_link_text('Sign in')
signInButton.click()
time.sleep(2)

# Click the new message button.
newMsgButton = edgeBrowser.find_element_by_css_selector('div.root-40 > button > span')
newMsgButton.click()
time.sleep(2)

# Compose the email.
toField = edgeBrowser.find_element_by_css_selector('input[aria-label="To"]')
toField.send_keys(sys.argv[1])                          
msgBody = edgeBrowser.find_element_by_css_selector('div[aria-label="Message body"]')
msgBody.send_keys(' '.join(sys.argv[2:]))
sendButton = edgeBrowser.find_element_by_css_selector('button[aria-label="Send"]')
sendButton.click()
time.sleep(2)

# Send email confirmation
confirmButton = edgeBrowser.find_element_by_css_selector('button[id="ok-1"]')
confirmButton.click()
print('Email Sent.')





