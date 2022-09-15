from common_features import CommonFeatures as CF
from locators.intro_page_locator import IntroStartButton as SB
import allure

class ChooseUserThatExists(CF):
    def __init__(self):
        pass

    @allure.step("Choose an option [Already member of Space]")
    def choose_user_exists(self):
        user_part_of_space = CF.find_element(self, SB.START_BUTTON)
        return user_part_of_space
