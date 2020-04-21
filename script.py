from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from getpass import getpass

import json
import random
import time

import os
import sys

def visitPage(email, password):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    
    driver.get("https://colab.research.google.com/notebooks/intro.ipynb")

    try:
        sign_in = driver.find_elements_by_xpath("//*[contains(text(), 'Sign in')]")[0]
        sign_in.click()

        email_box = driver.find_element_by_id("identifierId")
        email_box.send_keys(email)
        email_box.send_keys(Keys.ENTER)
    
        time.sleep(1)

        password_box = driver.find_element_by_name("password")
        password_box.send_keys(password)
        password_box.send_keys(Keys.ENTER)
    
        time.sleep(3)
        
        print("signed in")

        driver.get('https://colab.research.google.com/drive/19rP2swTDmJ05Bf6zjOK4gQFZoX1m7kAx')
         
        rand = random.randint(1, 4)
        time.sleep(60 * rand)

        driver.quit()
        print("visited page for %s minute[s]" % rand)
    except:
        print("did not visit page")
if __name__ == "__main__":
    if os.path.isfile("data.json"):
        f = open("data.json", "r")
        f_js = json.load(f)

        email = f_js["email"]
        password = f_js["password"]
        
        f.close()
    else:
        sys.stdout.write("\rEmail: ")
        email = input()
        password = getpass()

    visitPage(email, password)

