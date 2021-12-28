from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_items_message(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY_NOW), \
            "Items to buy now message is presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MASSAGE), \
            "Empty basket message is not presented, but should be"
