from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from wireless import Wireless

wireless = Wireless()

if not wireless.power():
	print('[ERROR] WiFi adapter is off.')
	sys.exit()

if wireless.current() != 'TESTING':
	print('[ERROR] Not connected to TESTING. This script will work on TESTING network only.')
	print('[INFO] Currently connected to the network ' + wireless.current())
	sys.exit()

options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

SITE = "http://172.16.1.230/" # You can use any http website here
browser.get(SITE)

try:
	browser.find_element_by_name('user.username')
except:
	print('[INFO] Already signed-in.')
	sys.exit()

username = browser.find_element_by_name('user.username')
username.click()
username.send_keys("mother") # YOUR USERNAME

password = browser.find_element_by_name('user.password')
password.click()
password.send_keys("fucker") # YOUR PASSWORD

browser.find_element_by_xpath("//input[@type='submit']").click()

time.sleep(0.1)
browser.find_element_by_xpath("//input[@type='submit']").click()

print("[SUCCESS] Login Complete")
