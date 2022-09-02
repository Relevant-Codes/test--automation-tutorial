from helpers.locators import SearchResultsPageLocators
from pages.BasePage import BasePage

class SearchResultsPage(BasePage):

    """Search results page action methods come here"""
    def result_count(self):
        element = self.driver.find_element(*SearchResultsPageLocators.RESULT_COUNT)
        return element.text