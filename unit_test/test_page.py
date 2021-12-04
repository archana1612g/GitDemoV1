# This class is updated by Archana
# email: name@gmail.com

import unittest

from PageObjectModel import page_object_model
# from page_object_model import page
from PageObjectModel.page_object_model import page


class test_page(unittest.TestCase):
    def setUp(self):
        '''
        This is a setup method
        :return: None
        '''
        self.chrome_path = "C:\WebDriver\Chrome\chromedriver.exe"
        self.url = page_object_model.url
        self.all_obj = page.HomePage(self.url, self.chrome_path)


    def test_Sign_In_Button(self):
        '''
        This test is for sign_in_button method
        :return:None
        '''
        self.all_obj.signin()

    def test_search_text(self):
        '''
        This test is for search_text method
        :return: None
        '''
        self.all_obj.send_text(text=page_object_model.TextSearch)

    def test_send_text(self):
        '''
        This test is for sent_text method
        :return: True
        '''
        assert self.all_obj.send_text(page_object_model.TextSearch1)

    def test_click_button(self):
        '''
        This test is for click_button method
        :return: True
        '''
        self.all_obj.click_button()

    def test_click_No_button(self):
        '''
        This test is for click_button method
        :return: True
        '''
        assert self.all_obj.click_button(page_object_model.wrong_button), "Button Not Found"

    # def test_click_button(self):
    #     '''
    #     This test is for click_button method
    #     :return: Assertion Result
    #     '''
    #     assert self.all_obj.click_button(page_object_model.SignInButton)

    def test_refresh(self):
        '''
        This test is for refresh method
        :return: NOne
        '''
        self.all_obj.refresh()

    def test_title(self):
        '''
        This test is for title method
        :return: None
        '''
        self.all_obj.title()
        print('printed title')

    def test_scroll(self):
        '''
        This test is for scroll method
        :return: None
        '''
        self.all_obj.scroll()

    def test_mouse_hover(self):
        '''
        This test is for mouse_hover method
        :return: None
        '''
        self.all_obj.mouse_hover(page_object_model.Country)

    def tearDown(self):
        '''
        Tear Down method
        :return: None
        '''
        print("Done")
        del self.all_obj
        #can not access driver
      #  self.all_obj.driver.close()
        print("Code Cleanup")
