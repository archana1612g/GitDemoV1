from constants import amazon_elements, flipkart_elements


class PageElement:
    def __init__(self, id):
        self.id = id

    @staticmethod
    def getSearchTextBoxID(SearchTextBoxID=None):
        return SearchTextBoxID

    def getSearchIconID(SearchIconID=None):
        return SearchIconID

    def getXpath(self, xpath=None):
        return xpath
