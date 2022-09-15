# This page is illustrated after providing the passowrd
import allure

from common_features import CommonFeatures as CF
from locators.otp_page_locator import YourTestOTP as OTP


class ExistingOtp(CF):
    def __init__(self):
        pass

    @allure.step("current OTP is static, you will need to provide generated one")
    def received_otp_after_auth(self):
        test_received_otp = CF.find_element(self, OTP.TEST_OTP)
        return test_received_otp

    @allure.step("If OTP is late, than re-send text will become active and you should be able to receive new otp")
    def resend_otp(self):
        test_resend_otp = CF.find_element(self, OTP.OTP_IS_LATE_RESEND)
        return test_resend_otp
