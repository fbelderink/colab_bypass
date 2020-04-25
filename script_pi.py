from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from getpass import getpass
from pyvirtualdisplay import Display

import json
import random
import time

import os
import sys
import re

dir = {0: Keys.NUMPAD0, 1 : Keys.NUMPAD1, 2 : Keys.NUMPAD2, 3: Keys.NUMPAD3, 4: Keys.NUMPAD4,
        5: Keys.NUMPAD5, 6: Keys.NUMPAD6, 7: Keys.NUMPAD7, 8: Keys.NUMPAD8, 9: Keys.NUMPAD9}

def visitPage(email, password, link):
    #display = Display(visible=1, size=(800, 600))
    #display.start()

    driver = webdriver.Chrome()
    
    driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent")

    #driver.get("https://colab.research.google.com/notebooks/intro.ipynb")
    
    driver.find_elements_by_xpath('//*[@id="openid-buttons"]/button[1]')[0].click()
    
    email_box = driver.find_element_by_xpath('//input[@type="email"]')
    driver.execute_script("arguments[0].value =  '%s'" % (email), email_box)
    email_box.send_keys(Keys.ENTER)
    
    time.sleep(3)
    
    password_box = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    driver.execute_script("arguments[0].value = '%s'" % (password), password_box)
    password_box.send_keys(Keys.ENTER)
    
    time.sleep(3)
     
    driver.get(link)

    rand = random.randint(1, 4)
    time.sleep(60 * rand)

    driver.quit()
    print("visited page for %s minute[s]" % rand)

if __name__ == "__main__":
    if os.path.isfile("data.json"):
        f = open("data.json", "r")
        f_js = json.load(f)

        email = f_js["email"]
        password = f_js["password"]
        link = f_js["link_notebook"]
        
        f.close()
    else:
        sys.stdout.write("\rEmail: ")
        email = input()
        password = getpass()
        sys.stdout.write("\rLink: ")
        link = input()
    while True:
        visitPage(email, password, link)
        time.sleep(15 * 60)
