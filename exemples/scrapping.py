#

from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver


web_page = 'http://www.twitter.com'
nameterm = "twittos"
passterm = "password"

driver = webdriver.Firefox()
driver.get(web_page)

name_box = driver.find_element_by_class_name("email-input")
name_box.send_keys(nameterm)

pass_box = driver.find_element_by_name("session[password]")
pass_box.send_keys(passterm)

submit = driver.find_element_by_class_name("EdgeButton")
submit.click()
