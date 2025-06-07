from selenium.webdriver.common.by import By
from Utils import navigate_link_text, fill_textbox, click_report, wait_until_url


class Registration:
    def __init__(self, driver):
        self.driver = driver


    def navigate_to_create_an_account(self):
        navigate_link_text(self.driver,"Create an Account")


    def fill_account_info(self, mail, password):
        fill_textbox(self.driver,"firstname",'Gill')
        fill_textbox(self.driver,"lastname",'Shalev')
        fill_textbox(self.driver,"email_address", mail)
        fill_textbox(self.driver,"password", password)
        fill_textbox(self.driver,"password-confirmation", password)
        create_btn = self.driver.find_elements(By.CSS_SELECTOR,"button[type='submit']")[1]
        click_report(create_btn, "submit and create an account")

        # Prints the website's message after successful registration
        wait_until_url(self.driver, "account/")
        span_text = self.driver.find_element(By.CSS_SELECTOR,"#maincontent > div.page.messages > div:nth-child(2) > div > div > div").text
        print("Website Message: ", span_text)


    def sign_out(self):
        signout_menu_btn = self.driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button")
        signout_menu_btn.click()
        signout_btn = self.driver.find_element(By.LINK_TEXT,"Sign Out")
        click_report(signout_btn, "sign out")
        print('Successfully Logged Out')





