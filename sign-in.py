from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from wireless import Wireless
import requests

# Checking WiFi adapter
wireless = Wireless()
if not wireless.power():
	print('WiFi adapter is off.')
	sys.exit()

if wireless.current() != 'TESTING':
	print('Not connected to TESTING. This script will work on TESTING network only.')
	print('Currently connected to the network ' + wireless.current())
	sys.exit()

# Checking if already signed-in
signedIn = False
try:
	req = requests.get('http://clients3.google.com/generate_204')
	if req.status_code != 204:
		raise Exception
	else:
		signedIn = True
except:
	pass

if signedIn:
	print('Already signed-in.')
	sys.exit()


# Sign In Precedure
options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

SITE = "http://172.16.1.230/" # You can use any http website here
browser.get(SITE)

username = browser.find_element_by_name('user.username')
username.click()
username.send_keys("mother") # YOUR USERNAME

password = browser.find_element_by_name('user.password')
password.click()
password.send_keys("fucker") # YOUR PASSWORD

browser.find_element_by_xpath("//input[@type='submit']").click()

time.sleep(0.1)
browser.find_element_by_xpath("//input[@type='submit']").click()

print("Sign-In Complete")

