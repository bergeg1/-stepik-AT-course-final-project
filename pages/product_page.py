from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_add_to_basket_button()

    def should_be_product_url(self):
        # реализуйте проверку на корректный url адрес Usage: driver.current_url
        print(f"current_url = '{self.browser.current_url}'")
        assert self.browser.current_url.find("?promo=") > -1, "Product URL is not correct"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def product_name_before_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_cost_before_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), "Product cost is not presented"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text

    def product_name_check_after_adding(self, product_name):
        # print(f"product_name_before_adding = '{product_name}'")
        # print(f"product_name_after_adding = '{self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TO_CHECK).text}'")
        assert product_name == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TO_CHECK).text, \
            "Product name changed after adding to basket"

    def basket_total_check_after_adding(self, product_cost):
        # print(f"product_cost_before_adding = '{product_cost}'")
        # print(f"basket_total_after_adding = '{self.browser.find_element(*ProductPageLocators.PRODUCT_COST_TO_CHECK).text}'")
        assert product_cost == self.browser.find_element(*ProductPageLocators.PRODUCT_COST_TO_CHECK).text, \
            "Basket total amount is not correct"
