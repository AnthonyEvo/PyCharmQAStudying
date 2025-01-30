from selenium import webdriver

def before_feature(context, feature):
    url = "ebay.com"
    print(f"Scenario URL set to {url}")
    context.URL = f"https://www.{url}"

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.get(context.URL)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()