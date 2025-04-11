from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


SEARCH_FIELD = (By.CSS_SELECTOR, '#search-field input[type="text"]')

@given('Open target main page')
def open_target_main(context):
    context.app.main_page.open_main_page()
    context.driver.wait.until(
        EC.element_to_be_clickable(SEARCH_FIELD),
        message='Search field not clickable'
    )

@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search(search_word)


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart_icon()
