import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object_model.elements import PageElement
from selenium.webdriver.support import expected_conditions as EC


class AmazonInSearch(unittest.TestCase):

    def test_search_mobile(self):
        self.driver.find_element_by_id(PageElement.find_elements_by_Id())
        # self.driver.find_element_by_id(PageElement.).send_keys(testdata.IPhoneXS)
        # self.driver.find_element_by_id(PageElement.SearchIconID).click()
        # WebDriverWait(self.driver, 0.5).until(EC.presence_of_element_located(PageElement.ApplePhoneXpath))
        # self.driver.find_element_by_xpath(PageElement.ApplePhoneXpath).click()
        return True

    # def test_amazon_best_sellers(self):
    #     self.driver.find_element_by_link_text('Best Sellers').click()
    #     print(self.driver.name)
    #     self.driver.find_element_by_link_text('Amazon Launchpad').click()
    #     print(self.driver.name)
    #     try:
    #         diya1 = self.driver.find_element_by_xpath(
    #             "@title='DesiDiya® Copper Fairy String Lights with USB Powered Led Light "
    #             "for Diwali Christmas Birthday Party Wedding Ceremony Bedroom and Balcony "
    #             "Home Decoration (10 Meters).'")
    #     except NoSuchElementException as e:
    #         print("Diya Name not found")
    #     diya1.click()
    #     print('Diya Found')
    #     print(self.driver.name)
    #     return True
    #
    # def test_amazon_electronics(self):
    #     self.driver.find_element_by_link_text('Electronics')
    #     print(self.driver.name)
    #     try:
    #         fitness_tracker = self.driver.find_element_by_link_text('Fitness trackers')
    #     except NoSuchElementException as e1:
    #         print("Fitness Tracker not found")
    #     fitness_tracker.click()
    #     print('Fitness Tracker Found')
    #     print(self.driver.name)
    #     return True

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
