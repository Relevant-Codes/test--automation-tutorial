import unittest
from selenium import webdriver

import pages.SearchResultsPage 
import pages.MainPage 

class SearchTests(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://selenium-training.relevantcodes.com/")

    def test_search_in_open_cart(self):
        """Tests OpenCart search feature. Searches for the word "iPhone" then
        verified that some results show up."""

        #Load the main page. In this case the home page of https://selenium-training.relevantcodes.com/.
        main_page = pages.MainPage.MainPage(self.driver)
        main_page.search("iPhone")
        
        result_page = pages.SearchResultsPage.SearchResultsPage(self.driver)
        print(result_page.result_count())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()