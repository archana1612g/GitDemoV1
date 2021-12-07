""" Page Object Model Package"""
#HomePage = str(input("enter HomePage Amazon/Facebook"))
HomePage = "Amazon"
if HomePage == "Amazon":
    import Amazon
    url = Amazon.AmazonURL
  #  url:str = "https://www.amazon.in/"
elif HomePage == "Facebook":
    import Facebook
    url = Facebook.FacebookURL
    #url:str = "https://www.facebook.in/"

chromepath: str = "C:\WebDriver\Chrome\chromedriver.exe"
SignInButton = "//span[@id='nav-link-accountList-nav-line-1']"
wrong_button = "//span[@class='nav-action-inner']"
Country = "//span[@class='icp-nav-flag icp-nav-flag-in']"
CancelButton = None
TextSearch = "//input[@id='twotabsearchtextbox']"
TextSearch1 = "//input[@id='twotabsearchtextbox']"
DataSearch = "Electronics"
search_button = "//input[@id='nav-search-submit-button']"

