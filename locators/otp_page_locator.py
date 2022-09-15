# In order to run following code, provide a mock otp
from appium.webdriver.common.appiumby import AppiumBy


class YourTestOTP():
    TEST_OTP = (AppiumBy.ID, "ge.space.app:id/passwordBaseFragmentPin")
    OTP_IS_LATE_RESEND = (AppiumBy.ID, "ge.space.app:id/passwordRemainderLabel")