from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys

options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

SITE = "http://172.16.1.230/" # You can use any http website here
browser.get(SITE)

try:
	browser.find_element_by_name('user.username')
except:
	print('Already signed-in.')
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

print("Login Complete")
