import allure

from common_features import CommonFeatures as CF
from locators.check_new_password_auth_page_locator import NewPasswordCheck as NCH


class NewPwdCheck(CF):
    def __init__(self):
        pass

    @allure.step("Authorize with new password")
    def new_password_auth(self):
        test_new_pwd_auth = CF.find_element(self, NCH.NEW_CODE_CHECK)
        return test_new_pwd_auth
