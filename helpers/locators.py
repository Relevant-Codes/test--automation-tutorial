from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    SEARCH_TEXTBOX = (By.NAME, 'search')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    RESULT_COUNT = (By.CLASS_NAME, 'row')


    pass