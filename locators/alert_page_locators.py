from appium.webdriver.common.appiumby import AppiumBy


class AlertsAfterAuthorization:
    ALERT_MESSAGE_FINGER_PRINT_SUGGESTION = (AppiumBy.ID, "ge.space.app:id/alertMessage")
    ALERT_NEGATIVE_BUTTON = (AppiumBy.ID, "ge.space.app:id/alertNegativeButton")

    INFO_ALERT_AFTER_FINGERPRINT_CANCEL = (AppiumBy.ID, "ge.space.app:id/alertMainView")
    INFO_ALERT_CANCEL = (AppiumBy.ID, "ge.space.app:id/alertDialogItemRootView")
