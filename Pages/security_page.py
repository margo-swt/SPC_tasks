import allure

from common_features import CommonFeatures as CF
from locators.security_page_locators import SecurityPageForPasswordChange as PWCH


class SecurityAccess(CF):
    def __init__(self):
        pass

    @allure.step("Select change password field")
    def choose_change_password(self):
        test_pwd_func = CF.find_element(self, PWCH.CHANGE_PASSWORD)
        return test_pwd_func
