from behave import fixture, use_fixture
from behave.model import ScenarioOutline
import copy
import csv
from utils.driver_factory import DriverFactory


def before_feature(context, feature):
    features = (scenario for scenario in feature.scenarios 
                if type(scenario) == ScenarioOutline and 'data_from_file' in scenario.tags)
    for scenario in features:
        for example in scenario.examples:
            orig = copy.deepcopy(example.table.rows[0])
            example.table.rows = []
            with open('data_for_tests/wrong_checkout_form_test_data.csv') as file:
                csv_reader = csv.reader(file, delimiter=';')
                for row in csv_reader:
                    n = copy.deepcopy(orig)
                    n.cells = [f'{row[0]}', f'{row[1]}', f'{row[2]}', f'{row[3]}']
                    example.table.rows.append(n)

@fixture
def selenium_browser_chrome(context):

    context.driver = DriverFactory.get_driver("chrome")
    context.driver.implicitly_wait(30)
    yield context.driver

    context.driver.quit()


@fixture
def selenium_browser_firefox(context):

    context.driver = DriverFactory.get_driver("firefox")
    context.driver.implicitly_wait(30)
    yield context.driver

    context.driver.quit()


def before_tag(context, tag):
    if tag == "fixture.browser.chrome":
        use_fixture(selenium_browser_chrome, context)
    elif tag == "fixture.browser.firefox":
        use_fixture(selenium_browser_firefox, context)


def before_all(context):
    context.config.setup_logging()
