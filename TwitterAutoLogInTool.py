import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs





username_string = "INPUT USERNAME HERE"
password_string = "INPUT PASSWORD HERE"

browser = webdriver.Chrome()
browser.get("https://twitter.com/login")

browser.implicitly_wait(1)

username_field = browser.find_element_by_class_name("js-username-field")
browser.implicitly_wait(1)
username_field.send_keys(username_string)
browser.implicitly_wait(1)
password = browser.find_element_by_class_name("js-password-field")
password.send_keys(password_string)

login_button = browser.find_element_by_class_name("EdgeButtom--medium")
login_button.click()
