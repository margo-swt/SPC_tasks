import allure

from common_features import CommonFeatures as CF
from locators.parameters_page_locators import ParametersSectionOnProfile as Params


class ParametersSectionPage(CF):
    def __init__(self):
        pass

    @allure.step("Parameters section from profile | choosing security")
    def security_section_for_pwd(self):
        test_security_info = CF.find_element(self, Params.SECURITY_SECTION)
        return test_security_info

    @allure.step("After pwd was changed successfuly, we will log out to verify changes")
    def log_out_functionalty(self):
        test_log_out = CF.find_element(self, Params.LOG_OUT)
        return test_log_out