from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

from Facebook.facebook_login import driver

class Fbook:

    def fbook1(self):

        usr = input('Enter Email Id:')
        pwd = input('Enter Password:')

        username_box = driver.find_element_by_id('email')
        username_box.send_keys(usr)
        print("Email Id entered")
        sleep(1)

        password_box = driver.find_element_by_id('pass')
        password_box.send_keys(pwd)
        print("Password entered")
        try:
            login_box = driver.find_element_by_id('loginbutton')
        except NoSuchElementException as e:
            print("exception block")
        login_box = driver.find_element_by_name('login')
        login_box.click()
        sleep(10)

    def fb2(self, x, y):
        return x + y
