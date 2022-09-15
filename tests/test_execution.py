import allure
from pytest_assume.plugin import assume

from Pages.intro_page import ChooseUserThatExists
from Pages.mobile_input_page import ExistingTestUserMobilePage
from Pages.passcode_page import ExistingTestUserPwdPage
from Pages.otp_page import ExistingOtp
from Pages.alert_page import ClassicAlerts
from Pages.go_to_profile_page import AuthUserProfile
from Pages.parameters_page import ParametersSectionPage
from Pages.security_page import SecurityAccess
from Pages.current_password_bf_change_page import CurrentPwdChangeFlow
from Pages.new_pwd_page import NewConfirmPassword
from Pages.success_button_page import SuccessfullyChangedButton
from Pages.card_activity_close_page import CartActClose
from Pages.check_new_password_auth_page import NewPwdCheck
import pytest

test_intro_page_spc = ChooseUserThatExists()
test_mobile_mock_user_spc = ExistingTestUserMobilePage()
test_user_pwd_spc = ExistingTestUserPwdPage()
test_user_otp_spc = ExistingOtp()
test_alerts_spc = ClassicAlerts()
test_profile_icon_spc = AuthUserProfile()
test_params_spc = ParametersSectionPage()
test_security_pwd_spc = SecurityAccess()
test_user_current_pwd_spc = CurrentPwdChangeFlow()
test_new_pwd_repeat_spc = NewConfirmPassword()
test_success_info_spc = SuccessfullyChangedButton()
test_close_cards_spc = CartActClose()
test_new_auth_spc = NewPwdCheck()


@allure.epic("Space app")
@allure.feature("Authorization with test user mobile")
@allure.story("Change and verify passcode")
class TestSpaceApp:

    @allure.title("Intro page - choose [Already a member]")
    def test_intro_page(self):
        user_exists_spc = test_intro_page_spc.choose_user_exists()
        with assume: assert user_exists_spc.is_clickable() == True
        user_exists_spc.click()

    @allure.title("Provide test user mobile number please")
    def test_member_mobile(self):
        test_user_spc = test_mobile_mock_user_spc.mobile_test_user()
        with assume: assert test_user_spc.is_displayed() == True
        with assume: assert test_user_spc.is_enabled() == True
        test_mobile = str(input('⚠️Enter test number: '))
        test_user_spc.send_keys(test_mobile)

    @allure.title("Provide test user password please and then we will change it")
    def test_member_code(self):
        test_password_spc = test_user_pwd_spc.test_user_pwd()
        with assume: assert test_password_spc.is_enabled() == True
        test_password = str(input('⚠️Enter test password: '))
        test_password_spc.send_keys(test_password)

    @allure.title("OTP should have been sent on provided number | if not, re-sent functionality will be activated")
    @pytest.mark.skipif(test_user_otp_spc.received_otp_after_auth().is_displayed() == False, reason="OTP is not always "
                                                                                                    "sent")
    def test_otp_received(self):
        test_otp_spc = test_user_otp_spc.received_otp_after_auth()
        resend_otp_spc = test_user_otp_spc.resend_otp()

        if test_otp_spc.is_displayed():
            test_otp_received = str(input('⚠️Enter test otp: '))
            test_otp_spc.click()
            test_otp_spc.send_keys(test_otp_received)
        elif resend_otp_spc.is_enabled():
            test_otp_received = str(input('⚠️Enter new otp: '))
            resend_otp_spc.click()
            resend_otp_spc.send_keys(test_otp_received)
        else:
            pass

    @allure.title("Alerts should be canceled | fingerprint")
    def test_catch_alerts_fingerprint(self):
        catch_alerts_fp_spc = test_alerts_spc.alert_messages()
        if catch_alerts_fp_spc.is_enabled():
            cancel_alert_first_proposal = test_alerts_spc.alert_messages_deny()
            cancel_alert_first_proposal.click()
        else:
            pass

    @allure.title("Alerts should be canceled | after fingerprint | info")
    def test_catch_alerts_info(self):
        catch_alerts_info_spc = test_alerts_spc.info_alert_check()
        if catch_alerts_info_spc.is_displayed():
            cancel_alert_second_proposal = test_alerts_spc.info_alert_cancel()
            cancel_alert_second_proposal.click()
        else:
            pass

    @allure.title("Steps to change passcode | select profile icon")
    def test_go_to_profile_icon(self):
        test_profile_spc = test_profile_icon_spc.go_to_user_profile()
        with assume: assert test_profile_spc.is_displayed()
        test_profile_spc.click()

    @allure.title("Go to security section")
    def test_security_page(self):
        test_parameters_spc = test_params_spc.security_section_for_pwd()
        assert test_parameters_spc.is_displayed()
        test_parameters_spc.click()

    @allure.title("Choosing change Password")
    def test_security_page_password_section(self):
        test_pwd_section_spc = test_security_pwd_spc.choose_change_password()
        assert test_pwd_section_spc.is_displayed()
        test_pwd_section_spc.click()

    @allure.title("enter your current password")
    def test_your_current_password(self):
        test_current_password_spc = test_user_current_pwd_spc.your_current_password()
        if test_current_password_spc.is_displayed():
            test_password = str(input('⚠️Enter your current password: '))
            test_current_password_spc.send_keys(test_password)

    @allure.title("enter your New password")
    def test_your_new_password(self):
        test_new_password_spc = test_new_pwd_repeat_spc.new_password_creation()
        if test_new_password_spc.is_displayed():
            test_password = str(input('⚠️Enter your new password: '))
            test_new_password_spc.send_keys(test_password)

    @allure.title("enter your New password")
    def test_your_new_password(self):
        test_repeat_password_spc = test_new_pwd_repeat_spc.new_password_repeat()
        if test_repeat_password_spc.is_displayed():
            test_password = str(input('⚠️Repeat your new password: '))
            test_repeat_password_spc.send_keys(test_password)

    @allure.title("enter your New password")
    def test_your_new_password_otp(self):
        test_new_password_otp_spc = test_new_pwd_repeat_spc.new_password_repeat_otp()
        if test_new_password_otp_spc.is_displayed():
            test_password = str(input('⚠ Did you receive OTP? Type here: '))
            test_new_password_otp_spc.send_keys(test_password)

    @allure.title("Success button")
    def test_successful_button(self):
        test_success_btn_spc = test_success_info_spc.success_page_interaction()
        with assume: assert test_success_btn_spc.is_enabled()
        test_success_btn_spc.click()

    @allure.title("Close params card and log out")
    def test_params_card_close(self):
        test_params_close_spc = test_close_cards_spc.card_act_close()
        with assume: assert test_params_close_spc.is_displayed()
        test_params_close_spc.click()
        self.test_go_to_profile_icon()
        with assume: assert test_params_spc.log_out_functionalty.is_displayed()
        test_params_spc.log_out_functionalty.click()

    @allure.title("Authorize with new Pwd")
    def test_auth_new_password(self):
        test_new_authorization_spc = test_new_auth_spc.new_password_auth()
        if test_new_authorization_spc.is_displayed():
            test_password = str(input('⚠️Repeat your new password: '))
            test_new_authorization_spc.send_keys(test_password)
