import allure

from common_features import CommonFeatures as CF
from locators.go_to_profile_page_locator import AuthProfile as PR


class AuthUserProfile(CF):
    def __init__(self):
        pass

    @allure.step("So far - user is already authorize now we need to change password | step 1 go to profile")
    def go_to_user_profile(self):
        test_profile_icon = CF.find_element(self, PR.PROFILE_ICON)
        return test_profile_icon
