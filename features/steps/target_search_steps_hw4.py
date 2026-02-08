
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]')
CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
BENEFIT_CELL = (By.CSS_SELECTOR, '[class="cell-item-content"]')
ADD_CART_BUTTON = (By.CSS_SELECTOR, '[id*="addToCartButtonOrTextIdFor"]')
ADD_CART_BUTTON_2 = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
ADD_CART_BUTTON_3 = (By.CSS_SELECTOR, '[href="/cart"]')
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@given('Open Target circle page')
def open_cart(context):
    context.driver.get('https://www.target.com/circle')
    sleep(3)


@then('Verify 10 or more benefit cells')
def verify_benefit_cells(context):
    actual_benefit_cells_len = context.driver.find_elements(*BENEFIT_CELL)
    print(f'Benefit cells: {len(actual_benefit_cells_len)}')
    assert len(actual_benefit_cells_len) >= 10, f'Benefit cells count {len(actual_benefit_cells_len)} should be greater or equal to 10'


@when('Add item to cart')
def add_to_cart(context):
    sleep(10)
    context.driver.find_element(*ADD_CART_BUTTON).click()
    sleep(3)
    context.driver.find_element(*ADD_CART_BUTTON_2).click()
    sleep(2)
    context.driver.find_element(*ADD_CART_BUTTON_3).click()


@then('Verify {item} in cart')
def verify_product_name(context, item):
    sleep(5)
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    print('Name in cart: ', product_name_in_cart)
    assert item in product_name_in_cart.lower(), \
        f'Expected {item} did not match {product_name_in_cart}'



