# Created by pauge at 8/20/2024
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, )

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(10)


@then('Verify correct search results shown')
def verify_search_results(context):
    expected_text = 'car'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify Empty cart message is shown')
def verify_empty_cart(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'


@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.ID, 'signin').click()
    sleep(2)


@then('Verify Sign in Form opens')
def verify_sign_in(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has correct product')
def verify_product_name(context):
    # context.product_name => stored before
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    print('Name in cart: ', product_name_in_cart)
    assert context.product_name[:20] == product_name_in_cart[:20], \
        f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'


@then('Verify item in cart')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"