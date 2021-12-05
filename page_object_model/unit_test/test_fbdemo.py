import unittest

from selenium import webdriver

from Facebook.FacebookDemo import Fbook


# import page

class FbDemo(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path = "C:\WebDriver\Firefox\geckodriver.exe")
        # self.driver = webdriver.Chrome("C:\WebDriver\Chrome\chromedriver.exe")
        pass

    # @staticmethod
    # def test_fb1():
    #     print("Test Facebook in Python")
    #     obj = Fbook()
    #     obj.fbook1()
    #     c = obj.fb2('x', 'y')
    #     assert c is int
    #     # print(self.driver.name)
    #     return True
    @staticmethod
    def test_fb1():
        obj = Fbook()
        # obj.fb1()
        b = obj.fb2(1, 2)
        assert b != 2
        # obj.fb2(1,'x')

    def tearDown(self):
        print("Done")
      # self.driver.quit()
        print("Code Cleanup")
