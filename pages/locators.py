from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '[href="/en-gb/basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_COST = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME_TO_CHECK = (By.CSS_SELECTOR, '[class ="alert alert-safe alert-noicon alert-success  fade in"] strong')
    PRODUCT_COST_TO_CHECK = (By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-info  fade in"] strong')


class BasketPageLocators:
    ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, '[class="col-sm-6 h3"]')
    EMPTY_BASKET_MASSAGE = (By.CSS_SELECTOR, 'p [href="/en-gb/"]')
