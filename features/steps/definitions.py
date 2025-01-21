from time import sleep

from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By

@step('Navigate to {site}')
def test(context, site):
    context.driver = webdriver.Chrome()
    context.driver.get(f"https://www.{site}")

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

@step('Search for {variable1} in {variable2}')
def search_for_element(context, variable1, variable2):
    result = context.driver.find_element(By.XPATH, f"//{variable2}//*[contains(text(), '{variable1}') or @aria-label = '{variable1}']")

# $x("//a[contains(text(), 'Brand Outlet') or @aria-label = 'Brand Outlet']")

@step('Open link {var1} in {var2}')
def open_selected_element(context, var1, var2):
    element = context.driver.find_element(By.XPATH, f"//{var2}//a[contains(text(), '{var1}') or @aria-label = '{var1}']")
    element.click()

@step('Verify {var1} in {var2} and go back to {var3}')
def verify_element(context, var1, var2, var3):
    sleep(5)
    element1 = context.driver.find_element(By.XPATH, f"//{var2}//*[contains(text(), '{var1}') or contains(text(), 'Please verify yourself') or @aria-label = '{var1}' or class = '{var1}']")
    element2 = context.driver.get(f"https://www.{var3}")
    sleep(5)