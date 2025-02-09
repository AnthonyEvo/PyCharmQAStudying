from time import sleep
from behave import step
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

import warnings
import datetime

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

sleep_time = 0
error_log = ""


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

    button_xpath = "//section[@class = 'gh-header__main']/form[@class = 'gh-search']//div[//span[text() = 'Search'] and @class = 'gh-search-button__wrap']/button"
    error_message = 'Button is not located'

    search_button = WebDriverWait(context.driver, sleep_time).until(expected_conditions.presence_of_element_located((By.XPATH, button_xpath)), error_message)
    search_button.click()

@step('Select filter {filter_name} in {filter_value} list')
def filter_select(context, filter_name, filter_value):

    element_xpath = f"//div[.//li/h3/div[contains(text(), '{filter_value}')]]//a[.//div/div/div/span[text() = '{filter_name}']]//input"
    error_message = "Element not found"

    element = WebDriverWait(context.driver, sleep_time).until(expected_conditions.presence_of_element_located((By.XPATH, element_xpath)), error_message)
    element.click()

@step('Get all items which not contains "{item_filter}" from 1 page')
def anomaly_search_at_page(context, item_filter):
    anomaly_search_at_few_pages(context, item_filter, 1)

@step('Get all items which not contains "{item_filter}" from {count} pages')
def anomaly_search_at_few_pages(context, item_filter, count):
    records = context.driver.find_elements(By.XPATH, "//li[starts-with(@class, 's-item')][parent::ul[starts-with(@class, 'srp-results') and not(contains(@class, 'carousel'))]][ancestor::div[starts-with(@role, 'main')]]//span[@role = 'heading']")
    page = 1
    while page <= int(count):
        print(f"--- Page {page} ---" )
        context.anomaly_counter = list_check(item_filter, records)
        context.driver.find_element(By.XPATH, "//a[@aria-label = 'Go to next search page']").click()
        page += 1
        records = context.driver.find_elements(By.XPATH,"//li[starts-with(@class, 's-item')][parent::ul[starts-with(@class, 'srp-results') and not(contains(@class, 'carousel'))]][ancestor::div[starts-with(@role, 'main')]]//span[@role = 'heading']")

def get_element_by_xpath(context, element_xpath):
    element = WebDriverWait(context.driver, sleep_time).until(expected_conditions.presence_of_element_located((By.XPATH, element_xpath)), f'Element not found by this XPath{element_xpath}')
    return element

def get_elements_by_xpath(context, element_xpath):
    elements = WebDriverWait(context.driver, sleep_time).until(expected_conditions.presence_of_element_located((By.XPATH, element_xpath)), f'No elements found by this XPath{element_xpath}')
    if elements is not None: elements = context.driver.find_elements(By.XPATH, element_xpath)
    return elements

def list_check(item_filters, records):
    anomalies_count = 0
    for record in records:
        is_filtered = False
        for item_filter in item_filters:
            if item_filter.lower() not in record.text.lower():
                warnings.warn(f"Anomaly detected: {record.text} num. {records.index(record)} not contains {item_filter}")
                write_to_error_log(f"Anomaly detected: {record.text} num. {records.index(record)} not contains {item_filter}\n")
                anomalies_count += 1
                is_filtered = True
                break
        if not is_filtered: print(f"Successfully detect {item_filters} in {record.text} num. {records.index(record)}")

    return anomalies_count

@step("start, set default sleep time to {time}")
def step_impl(context, time):
    global sleep_time
    sleep_time = int(time)

@step("Use smart filter, page quantity is {page_count}")
def smart_filter(context, page_count):
    # get filters from behave script
    page = 1
    filter_list = context.table

    # turn on filters on webpage
    for message in filter_list:
        filter_select(context, message["Filter_value"], message["Filter_name"])

    search_result_xpath = "//li[starts-with(@class, 's-item')][parent::ul[starts-with(@class, 'srp-results') and not(contains(@class, 'carousel'))]][ancestor::div[starts-with(@role, 'main')]]//span[@role = 'heading']"
    records = get_elements_by_xpath(context, search_result_xpath)
    print(f'Got {len(records)} search results from the page')

    filter_values = list()
    for filter_raw in filter_list:
        filter_values.append(filter_raw["Filter_value"])

    while page <= int(page_count):
        print(f"--- Page {page} ---")
        context.anomaly_counter += list_check(filter_values, records)

        try: get_element_by_xpath(context, "//a[@aria-label = 'Go to next search page']").click()
        except NoSuchElementException as ex: warnings.warn(f'Quantity of pages equal to {page} or element xPath is wrong')

        page += 1
        records = get_elements_by_xpath(context, search_result_xpath)
        print(f'Got {len(records)} search results from the page')

    if context.anomaly_counter > 0:
        warnings.warn(f'Test detects {context.anomaly_counter} anomalies')
        raise Exception(f'Test detect {context.anomaly_counter} anomalies')

    # gather data from webpage and check for filters mismatches

def write_to_error_log(message):
    global error_log
    error_log += f'{datetime.datetime.now()} {message}'