import unittest

from selenium import webdriver


# import page

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = "C:\WebDriver\Firefox\geckodriver.exe")
        self.driver.get("http://www.python.org")

    @staticmethod
    def test_search_in_python_org():
        print("test search in python")
       # print(self.driver.name)
       # return True


    def test_print_driver_name(self):
        print(self.driver.name)
       # return True

    def tearDown(self):
        print("tear down=clean up")
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
