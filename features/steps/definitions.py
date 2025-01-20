from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By


@step('Navigate to Google')
def test(context):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

@step('Go to ebay.com')
def test(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.ebay.com")

@step('In search field type "iPhone"')
def test_def(context):
    element = context.driver.find_element(By.ID, "gh-ac")
    element.send_keys("iPhone")

@step('In search field type "Dress"')
def search_dress(context):
    element = context.driver.find_element(By.ID, "gh-ac")
    element.send_keys("dress")

@step('Click the "Search"')
def test_def(context):
    search_button = context.driver.find_element(By.XPATH, "//input[@value = 'Search']")
    search_button.click()

@step('the first result item is "iPhone"')
def validate_first_result(context):
    result = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Apple iPhone SE 3rd')]")
