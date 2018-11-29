#2018-11-26
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json

browser = webdriver.Chrome()
browser.maximize_window()
#driver = webdriver.Firefox()
#browser.get("http://login.taobao.com")
#windows 用Keys.CONTROL 如同ctrl+t
#browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'T')
browser.get("http://www.amazon.com")

js='window.open("http://www.google.com");'
browser.execute_script(js)
print(js)
#driver.get('http://mm.taobao.com/')
url = "http://www.baidu.com"
js_1 = 'window.open("'+ url + '");'
browser.execute_script(js_1)
print("js_1 is :",js_1)