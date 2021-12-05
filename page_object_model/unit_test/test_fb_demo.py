import unittest

from facebook.FacebookDemo import Fbook


# import page

class test_fb(unittest.TestCase):
    def setUp(self):
        pass
        # self.driver = webdriver.Firefox(executable_path = "C:\WebDriver\Firefox\geckodriver.exe")
        # self.driver.get("http://www.python.org")

    @staticmethod
    def test_fb1():
        obj = Fbook()
        # obj.fb1()
        b = obj.fb2(1, 2)
        assert b != 2
        # obj.fb2(1,'x')

    # print("test search in python")
    # print(self.driver.name)
    # return True

    def tearDown(self):
        print("tear down=clean up")
        # self.driver.close()


if __name__ == "__main__":
    unittest.main()
