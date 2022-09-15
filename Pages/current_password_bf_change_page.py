import allure

from common_features import CommonFeatures as CF
from locators.current_password_bf_change_page_locators import CurrentPwdChange as CUR


class CurrentPwdChangeFlow(CF):
    def __init__(self):
        pass

    @allure.step("Provide current password")
    def your_current_password(self):
        test_current_bf = CF.find_element(self, CUR.CURRENT_PWD)
        return test_current_bf
