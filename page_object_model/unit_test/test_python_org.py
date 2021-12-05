import unittest

from selenium import webdriver


# import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path = "C:\WebDriver\Firefox\geckodriver.exe")
        self.driver = webdriver.Chrome("C:\WebDriver\Chrome\chromedriver.exe")
        self.driver.get("http://www.python.org")

    @staticmethod
    def test_search_in_python_org():
        print("Test Search in Python")
        # print(self.driver.name)
        return True

    def test_search_printname_for_python(self):
        print(self.driver.name)
        return True

    def tearDown(self):
        self.driver.close()
        print("Code Cleanup")


if __name__ == "__main__":
    unittest.main()
