from time import sleep
from behave import step
from selenium.webdriver.common.by import By

sleep_time = 0

@step('Set scenario URL as {url}')
def set_url_for_scenario(context, url):
    print(f"Scenario URL set to {url}")
    context.URL = f"https://www.{url}"


@step('In search field type {request}')
def search_for_request(context, request):
    element = context.driver.find_element(By.ID, "gh-ac")
    element.send_keys(request)

    #   $x("//section[@class = 'gh-header__main']/form[@class = 'gh-search']//div[//span[text() = 'Search'] and @class = 'gh-search-button__wrap']/button")

@step('Click the "Search" button')
def test_def(context):
    search_button = context.driver.find_element(By.XPATH, "//section[@class = 'gh-header__main']/form[@class = 'gh-search']//div[//span[text() = 'Search'] and @class = 'gh-search-button__wrap']/button")
    search_button.click()

@step('the first result item is "iPhone"')
def validate_first_result(context):
    result = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Apple iPhone SE 3rd')]")

@step('Search for {variable1} in {variable2}')
def search_for_element(context, variable1, variable2):
    sleep(3)
    result = context.driver.find_element(By.XPATH, f"//{variable2}//*[contains(text(), '{variable1}') or @aria-label = '{variable1}']")

    #   $x("//a[contains(text(), 'Brand Outlet') or @aria-label = 'Brand Outlet']")

@step('Open link {var1} in {var2}')
def open_selected_element(context, var1, var2):
    sleep(8)
    element = context.driver.find_element(By.XPATH, f"//{var2}//a[contains(text(), '{var1}') or @aria-label = '{var1}']")
    element.click()

@step('Verify {var1} in {var2} and go back to {var3}')
def verify_element(context, var1, var2, var3):
    sleep(sleep_time)
    element1 = context.driver.find_element(By.XPATH, f"//{var2}//*[contains(text(), '{var1}') or contains(text(), 'Please verify yourself') or @aria-label = '{var1}' or class = '{var1}']")
    element2 = context.driver.get(f"https://www.{var3}")
    sleep(sleep_time)

    #   / /div[.//li/h3/div[contains(text(), 'Network')]]//a[.//div/div/div/span[text() = 'Unlocked']]//input

@step('Select filter {filter_name} in {filter_list} list')
def filter_select(context, filter_name, filter_list):
    sleep(sleep_time)
    element = context.driver.find_element(By.XPATH, f"//div[.//li/h3/div[contains(text(), '{filter_list}')]]//a[.//div/div/div/span[text() = '{filter_name}']]//input")
    element.click()

@step('Every item is {condition} for first {page_num} pages')
def check_fe_pages(context, condition, page_num):
    current_page = context.driver.find_element(By.XPATH, "//ol//a[@aria-current]").text

@step('Get all items which not contains "{item_filter}" from 1 page')
def anomaly_search_at_page(context, item_filter):
    anomaly_search_at_few_pages(context, item_filter, 1)

@step('Get all items which not contains "{item_filter}" from {count} pages')
def anomaly_search_at_few_pages(context, item_filter, count):
    records = context.driver.find_elements(By.XPATH, "//li[starts-with(@class, 's-item')][parent::ul[starts-with(@class, 'srp-results') and not(contains(@class, 'carousel'))]][ancestor::div[starts-with(@role, 'main')]]//span[@role = 'heading']")
    page = 1
    while page <= int(count):
        print(f"--- Page {page} ---" )
        list_check(item_filter, records)
        context.driver.find_element(By.XPATH, "//a[@aria-label = 'Go to next search page']").click()
        page += 1
        records = context.driver.find_elements(By.XPATH,"//li[starts-with(@class, 's-item')][parent::ul[starts-with(@class, 'srp-results') and not(contains(@class, 'carousel'))]][ancestor::div[starts-with(@role, 'main')]]//span[@role = 'heading']")

def list_check(item_filter, records):
    for record in records:
        if item_filter.lower() not in record.text.lower():
            print(record.text)
        else:
            print(f"Anomaly detected: {record.text}")

@step("go set default sleep time to {time}")
def step_impl(context, time):
    global sleep_time
    sleep_time = int(time)