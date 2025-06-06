from selenium.webdriver.common.by import By

from Project_Automation.Utils import navigate_link_text, fill_textbox, click_report


class Login:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login(self):
        navigate_link_text(self.driver,"Sign In")

    def fill_saved_account_info(self, user_mail, user_password):
        fill_textbox(self.driver,"email",user_mail)
        fill_textbox(self.driver,"pass",user_password,'Password')
        signin_btn = self.driver.find_element(By.ID,'send2')
        click_report(signin_btn, "Sign in")
        print('successfully logged in')




