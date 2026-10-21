import pytest 
import time
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from config import Config
from playwright.sync_api import expect

def test_product_search(page):

    home_page = HomePage(page)
    search_results_page = SearchResultsPage(page)

    config_page = Config()
    product_name = config_page.product_name

    #OR
    # product_name = Config.product_name()

    home_page.enter_product_name(product_name)
    home_page.click_search()

    expect(search_results_page.get_search_results_page_header()).to_be_visible(timeout=3000)
    expect(search_results_page.is_product_exist(product_name)).to_be_visible(timeout=3000)
