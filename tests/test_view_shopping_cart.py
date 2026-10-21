import pytest 
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from config import Config

def test_view_shopping_cart(page):

    homepage = HomePage(page)
    searchpage = SearchResultsPage(page)
    productpage = ProductPage(page)

    configpage = Config()
    product_name = configpage.product_name
    product_quantity = configpage.product_quantity

    homepage.enter_product_name(product_name)
    homepage.click_search()

    title = searchpage.get_search_results_page_header()
    expect(title).to_be_visible(timeout=3000)

    product_count = searchpage.get_product_count()

    product = searchpage.is_product_exist(product_name)
    expect(product).to_be_visible(timeout=300)

    print("Total products ==>",product_count)

    product_page = searchpage.select_product(product_name)

    product_page.set_quantity(product_quantity)
    product_page.add_to_cart()
    expect(product_page.get_confirmation_message()).to_be_visible()

    product_page.click_items_to_navigate_to_cart()    

    shopping_cart_page = product_page.click_view_cart()
    expect(shopping_cart_page.is_page_loaded()).to_be_visible(timeout=3000)

    total_price = shopping_cart_page.get_total_price()
    print("Total shopping price ===> ",total_price)

    shopping_cart_page.click_on_checkout()