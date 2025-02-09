import os.path
import re
import warnings
import shutil

from selenium import webdriver

currentFeatureName = ''
currentScenarioName = ''
fails_directory_path = str()


def before_all(context):
    global fails_directory_path
    proj_location = os.path.dirname(__file__)
    fails_directory_path = os.path.join(proj_location, 'Test_fails')

    try:
        os.makedirs(fails_directory_path)
    except FileExistsError as ex:
        ...
    clean_directory(fails_directory_path)


def clean_directory(directory_path):
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except FileNotFoundError as Ex:
            ...


def after_step(context, step):
    if step.status == 'failed':
        adapted_name = name_adaptation(step.name)
        try:
            os.makedirs(os.path.join(fails_directory_path, f'{currentFeatureName}_fails'))
        except FileExistsError as ex:
            ...

        save_location = os.path.join(fails_directory_path, f'{currentFeatureName}_fails',
                                     f'{currentScenarioName}_{adapted_name}.png')
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
    context.driver.close()
    context.driver.quit()


def name_adaptation(name):
    adapted_name = f'{'_'.join(re.findall(r'\w+', name))}'
    return adapted_name
