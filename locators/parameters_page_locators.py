from appium.webdriver.common.appiumby import AppiumBy


class ParametersSectionOnProfile:
    SECURITY_SECTION = (AppiumBy.ID, "ge.space.app:id/profileSecurityArrow")
    LOG_OUT = (AppiumBy.ID, "app:id/contractRootView")
