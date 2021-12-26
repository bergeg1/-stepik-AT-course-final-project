from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_COST = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME_TO_CHECK = (By.CSS_SELECTOR, '[class ="alert alert-safe alert-noicon alert-success  fade in"] strong')
    PRODUCT_COST_TO_CHECK = (By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-info  fade in"] strong')
