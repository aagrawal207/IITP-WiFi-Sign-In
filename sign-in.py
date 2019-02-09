from selenium import webdriver
import time

browser = webdriver.Chrome()
site = "http://172.16.1.230" # You can use any http website or porn website
browser.get(site)

username = browser.find_element_by_name('user.username')
username.click()
username.send_keys("mother") # YOUR USERNAME

password = browser.find_element_by_name('user.password')
password.click()
password.send_keys("fucker") # YOUR PASSWORD

browser.find_element_by_xpath("//input[@type='submit']").click()

time.sleep(0.1)
browser.find_element_by_xpath("//input[@type='submit']").click()
