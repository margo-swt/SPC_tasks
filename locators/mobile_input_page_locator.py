from appium.webdriver.common.appiumby import AppiumBy


class ProvideTestUserNumber():
    TEST_USER_MOBILE = (AppiumBy.XPATH, "//android.widget.LinearLayout["
                                        "@resource-id='ge.space.app:id/editTextWithTitleEditTextContainer']//android"
                                        ".widget.EditText")
