from appium.webdriver.common.appiumby import AppiumBy


class NewPassword:
    # TODO review locators
    NEW_CODE = (AppiumBy.ID, "ge.space.app:id/passwordBaseFragmentPin")
    REPEAT_CODE = (AppiumBy.ID, "00000000-0000-024c-ffff-ffff00000473")

    OTP_AFTER_NEW_PWD_CONFIRM = (AppiumBy.ID, "ge.space.app:id/spCardFragmentOtpPinView")
