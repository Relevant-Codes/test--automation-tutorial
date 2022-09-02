from helpers.locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
from pages.BasePage import BasePage

class MainPage(BasePage):
    """Home page action methods come here."""

    def search(self, searchText):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.SEARCH_TEXTBOX)
        element.send_keys(searchText + Keys.ENTER)