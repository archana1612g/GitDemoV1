# This class is updated by Archana
# email: name@gmail.com


"""This module is used to create pages. """
from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from PageObjectModel import page_object_model
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjectModel.page_object_model.BaseLogger import logclass


class Page(object):
    """
    This class is used to assign driver and get webpage url.
    """

    def __init__(self, **kwargs):
        """
        :param url: string
        :param chrome_path: string
        Class constructor used to initialize driver and get url
        return: None
        """

       # self.log = logging.getLogger(__name__)
        print(kwargs)
        url = page_object_model.url
        web_driver_path = page_object_model.chromepath
        #url = kwargs.get('url')
        #web_driver_path = kwargs.get('web_driver_path')
        if (type(url), type(web_driver_path)) != (str, str):
            print("Please enter correct url")
            exit()
        self.driver = webdriver.Chrome(web_driver_path)
        self.driver.get(url)
        self.driver.maximize_window()
        self.log = logclass.get_logger(self)

    def __del__(self):
        """
        Closing the driver
        :return: None
        """
        print("Closing Driver")
        self.driver.close()


class HomePage(Page):
    """Home page action methods come here. I.e. Python.org"""

    def __init__(self, url=page_object_model.url, web_driver_path=page_object_model.chromepath):
        super().__init__(url=url, web_driver_path=web_driver_path)
        self.text_search = None

    def search_text(self, text_search: str = None):
        """
        :param text_search: string
        Returning Text to search
        :return: TextSearch : string
        """
        try:
            if text_search is None:
                self.text_search = page_object_model.TextSearch
            else:
                self.text_search = text_search
                self.click_button(page_object_model.search_button)
        except Exception as ex:
            self.log.error(ex)
        return self.text_search

    def send_text(self, text: Any = None):
        """
        :param text:
        :return: Boolean
        """
        status = None
        if text is None:
            text = self.search_text(page_object_model.TextSearch)
        else:
            print(text)
        try:
            if (self.driver.find_element(by=By.XPATH, value=text).send_keys(page_object_model.DataSearch)) is None:
                status = True
                print("Sent Text successful")
        except Exception as ex:
            self.log.info(ex)
            status = False
        return status

    def signin(self, SignInButton=None):
        '''
        This function is for clicking on Sign In Button on Amazon or Facebook
        :param SignInButton:
        :return:True if the button is clicked
        '''
        try:
            if SignInButton == None:
                SignInButton = page_object_model.SignInButton
            else:
                self.SignInButton = SignInButton
                print("clicked sign in successfully")

        except Exception as ex:
            self.log.error(ex)
        return self.click_button(SignInButton)

    def click_button(self, Button=None):
        '''
        This function is to click any button which is passed as a parameter
        :param Button:
        :return:True/False
        '''
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Button)))
            print("explicit wait is run")
            self.driver.find_element_by_xpath(Button).click()
            return True
        except Exception as ex:
            self.log.info(ex)
            return False

    def refresh(self):
        '''
         This funtion refreshes the Page
        :return: refreshed the webpage
        '''
        try:
            print("refreshed the page")
            return self.driver.refresh()
        except Exception as ex:
            self.log.warning(ex)

    def title(self):
        '''
        This function returns the title of the current Page
        :return:
        '''
        try:
            print(self.driver.title)
            return self.driver.title
        except Exception as ex:
            self.log.warning(ex)

    def scroll(self):
        '''
        This function is used to scroll down the complete body height or a specific height.
        :return:None
        '''
        try:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        except Exception as ex:
            self.log.info(ex)
        print("scrolled the page successfully")

    def mouse_hover(self, element=None):
        '''
        Hovers over the element
        :param element:
        :return:
        '''
        try:
            hover = self.driver.find_element_by_xpath(element)
            ele = ActionChains(self.driver).move_to_element(hover).perform()
            print("hovered over the element successfully")
            self.click_button(ele)
            print("clicked on the hovered element")
        except Exception as ex:
            self.log.error(ex)
            return False


if __name__ == "__main__":
    hp = HomePage()
    hp.send_text(text=page_object_model.TextSearch)
    hp.mouse_hover(page_object_model.Country)
    hp.search_text(page_object_model.TextSearch)
    hp.signin()
    hp.refresh()
    hp.title()
    hp.scroll()
