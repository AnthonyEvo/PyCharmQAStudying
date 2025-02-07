import os.path
import re
import warnings

from selenium import webdriver

currentFeatureName = ''
currentScenarioName = ''

def after_step(context, step):
    if step.status == 'failed':

        proj_location = os.path.dirname(__file__)
        adapted_name = name_adaptation(step.name)
        save_directory = os.path.join(proj_location, 'Test_fails', f'{currentFeatureName}_fails')

        try: os.makedirs(save_directory)
        except FileExistsError as ex: ...

        save_location = os.path.join(save_directory, f'{currentScenarioName}_{adapted_name}.png')
        warnings.warn(f'Saving fail screenshot to {save_location}')
        context.driver.save_screenshot(save_location)


def before_feature(context, feature):
    global currentFeatureName
    context.anomaly_counter = 0
    currentFeatureName = name_adaptation(feature.name)
    url = "ebay.com"
    print(f"Scenario URL set to {url}")
    context.URL = f"https://www.{url}"

def before_scenario(context, scenario):
    global currentScenarioName
    currentScenarioName = name_adaptation(name_adaptation(scenario.name))

    context.driver = webdriver.Chrome()
    context.driver.get(context.URL)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    if context.anomaly_counter > 0:
        warnings.warn(f'Test detects {context.anomaly_counter} anomalies')
        raise Exception(f'Test detect {context.anomaly_counter} anomalies')
    context.driver.quit()

def name_adaptation(name):
    adapted_name = f'{'_'.join(re.findall(r'\w+', name))}'
    return adapted_name