# Created by pauge at 8/20/2024
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]')
CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")



@given('Open Target circle page')
def open_cart(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')


@when('Identify one benefit cell')
def identify_benefit_cell(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify 10 or more benefit cells')
def verify_benefit_cells(context):
    context.driver.find_element(*CART_SUMMARY).click()


@when('Add item to cart')
def add_cart(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify cart has correct product')
def verify_product_name(context):
    # context.product_name => stored before
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    print('Name in cart: ', product_name_in_cart)
    assert context.product_name[:20] == product_name_in_cart[:20], \
        f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'


@then('Verify item in cart')
def verify_cart_items(context, amount):
    context.driver.get('https://www.target.com/cart')
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"