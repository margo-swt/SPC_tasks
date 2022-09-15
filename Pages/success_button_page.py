import allure

from common_features import CommonFeatures as CF
from locators.success_button_page_locator import SuccessButton as SB


class SuccessfullyChangedButton(CF):
    def __init__(self):
        pass

    @allure.step("You will see a success page and close it")
    def success_page_interaction(self):
        test_success_btn = CF.find_element(self, SB.SUCCESSFULLY_CHANGED)
        return test_success_btn
