from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

usr = input('Enter Login Id:')
pwd = input('Enter Password:')

driver = webdriver.Chrome("C:\WebDriver\Chrome\chromedriver.exe")
driver.get('https://www.facebook.com/')
print("Opened facebook")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print("Login Id entered")
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("Password entered")
sleep(1)

try:
    login_box = driver.find_element_by_id('loginbutton')
except NoSuchElementException as e:
    print(e, "Error in finding Login Button")
    login_box = driver.find_element_by_name('login')

login_box.click()
sleep(5)

driver.save_screenshot("ss.png")
driver.find_element_by_class_name('hu5pjgll lzf7d6o1').click()
driver.find_element_by_link_text('Log Out').click()
print("Done")
input('Press anything to quit')
driver.quit()
print("Finished")
