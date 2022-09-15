import conftest
from conftest import RemoteDriverCaps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonFeatures(RemoteDriverCaps):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time_out=50):
        try:
            wait = WebDriverWait(self.driver, time_out)
            element = wait.until(EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            raise e
