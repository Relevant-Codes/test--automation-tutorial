from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultsPage(BasePage):

    RESULT_COUNT = (By.CLASS_NAME, 'text-right')

    """Search results page action methods come here"""
    def result_count(self):
        element = self.driver.find_element(*self.RESULT_COUNT)
        return element.text