from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class MainPage(BasePage):

    SEARCH_TEXTBOX = (By.NAME, 'search')

    """Home page action methods come here."""

    def search(self, searchText):
        """Triggers the search"""
        element = self.driver.find_element(*self.SEARCH_TEXTBOX)
        element.send_keys(searchText + Keys.ENTER)