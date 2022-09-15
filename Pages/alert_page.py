# This page is illustrated after providing the pwd
import allure

from common_features import CommonFeatures as CF
from locators.alert_page_locators import AlertsAfterAuthorization as ALERT


class ClassicAlerts(CF):
    def __init__(self):
        pass

    @allure.step("Verify Alert Message")
    def alert_messages(self):
        test_first_alert = CF.find_element(self, ALERT.ALERT_MESSAGE_FINGER_PRINT_SUGGESTION)
        return test_first_alert

    @allure.step("Deny Alert Proposals")
    def alert_messages_deny(self):
        test_alert_cancel = CF.find_element(self, ALERT.ALERT_NEGATIVE_BUTTON)
        return test_alert_cancel

    @allure.step("After fingerprint alert will be denied, an info type of alert will appear and we should deny it too")
    def info_alert_check(self):
        test_info_alert = CF.find_element(self, ALERT.INFO_ALERT_AFTER_FINGERPRINT_CANCEL)
        return test_info_alert

    @allure.step("deny it info alert after fingerprint")
    def info_alert_cancel(self):
        test_info_alert_cancel = CF.find_element(self, ALERT.INFO_ALERT_CANCEL)
        return test_info_alert_cancel
