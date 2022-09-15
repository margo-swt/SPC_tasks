import allure

from common_features import CommonFeatures as CF
from locators.mobile_input_page_locator import ProvideTestUserNumber as UN


class ExistingTestUserMobilePage(CF):
    def __init__(self):
        pass

    @allure.step("You have to replace credentials with your test user")
    def mobile_test_user(self):
        test_mobile = CF.find_element(self, UN.TEST_USER_MOBILE)
        return test_mobile
