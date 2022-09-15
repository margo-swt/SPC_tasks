import allure

from common_features import CommonFeatures as CF
from locators.new_pwd_page_locator import NewPassword as NPW


class NewConfirmPassword(CF):
    def __init__(self):
        pass

    @allure.step("Provide new password ")
    def new_password_creation(self):
        test_new_pwd = CF.find_element(self, NPW.NEW_CODE)
        return test_new_pwd

    @allure.step("repeat new password it")
    def new_password_repeat(self):
        test_new_pwd_repeat = CF.find_element(self, NPW.REPEAT_CODE)
        return test_new_pwd_repeat

    @allure.step("OTP code received")
    def new_password_repeat_otp(self):
        test_new_pwd_repeat_otp = CF.find_element(self, NPW.NEW_CODE)
        return test_new_pwd_repeat_otp
