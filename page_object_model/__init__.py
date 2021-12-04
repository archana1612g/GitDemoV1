""" Page Object Model Package"""
#HomePage = str(input("enter HomePage Amazon/Facebook"))
HomePage = "Amazon"
if HomePage == "Amazon":
    import Amazon
    url = Amazon.AmazonURL
  #  url:str = "https://www.amazon.in/"
elif HomePage == "Facebook":
    from PageObjectModel import Facebook
    url = Facebook.FacebookURL
    #url:str = "https://www.facebook.in/"

chromepath = "C:\WebDriver\Chrome\chromedriver.exe"
SignInButton = "//span[@class='nav-action-inner']"
wrong_button = "//span[@class='nav-action-inner123']"
Country = "//span[@class='icp-nav-flag icp-nav-flag-in']"
CancelButton = None
TextSearch = "//input[@id='twotabsearchtextbox']"
TextSearch1 = "//input[@id='twotabsearchtextbox123']"
DataSearch = "Electronics"
search_button = "//input[@id='nav-search-submit-button']"

