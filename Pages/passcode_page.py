import allure

from common_features import CommonFeatures as CF
from locators.passcode_page_locator import PassCodePage as CP


class ExistingTestUserPwdPage(CF):
    def __init__(self):
        pass

    @allure.step("You will be redirected into password page , as long as the user is already a member.")
    def test_user_pwd(self):
        test_mobile_user_pwd = CF.find_element(self, CP.EXISTING_CODE_FIELD)
        return test_mobile_user_pwd
