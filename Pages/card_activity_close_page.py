import allure

from common_features import CommonFeatures as CF
from locators.card_activity_close_page_locator import CardCloseAct as CA


class CartActClose(CF):
    def __init__(self):
        pass

    @allure.step("after success page close card")
    def card_act_close(self):
        test_card_close = CF.find_element(self, CA.CARD_ACT)
        return test_card_close
