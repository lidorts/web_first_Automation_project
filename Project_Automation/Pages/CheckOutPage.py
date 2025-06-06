import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.core import driver

from Project_Automation.Utils import (navigate_link_text, fill_textbox, click_report, wait_until_visible, wait_until_url
, wait_until_invisible)


class Checkout:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_info(self):
        wait_until_url(self.driver, "#shipping")
        fill_textbox(self.driver,"company",'John Bryce', "",By.NAME)
        wait_until_visible(self.driver, By.NAME, "street[0]")
        fill_textbox(self.driver, "street[0]", 'Jabotinsky Street', "",By.NAME)
        wait_until_visible(self.driver, By.NAME, "street[1]")
        fill_textbox(self.driver, "street[1]", '3-rd floor, apartment 12', "",By.NAME)
        wait_until_visible(self.driver, By.NAME, "city")
        fill_textbox(self.driver, "city", 'Petah-Tikva', "",By.NAME)
        wait_until_visible(self.driver, By.NAME, "postcode")
        fill_textbox(self.driver, "postcode", '4960045', "",By.NAME)

        county_checkout_btn = self.driver.find_element(By.NAME, "country_id")
        select = Select(county_checkout_btn)
        select.select_by_visible_text("Israel")

        fill_textbox(self.driver, "telephone", '054-2330398', "",By.NAME)
        wait_until_visible(self.driver,By.XPATH, "//*[@id='shipping-method-buttons-container']/div/button")
        next_btn = self.driver.find_element(By.XPATH,"//*[@id='shipping-method-buttons-container']/div/button")
        click_report(next_btn,"Next Button")
        print('Successfully Filled Checkout Info')


    def place_order(self):
        wait_until_url(self.driver,"#payment")
        wait_until_invisible(self.driver, By.CSS_SELECTOR, ".loading-mask")

        wait_until_visible(self.driver, By.CSS_SELECTOR, "button.action.primary.checkout")
        place_order_btn = self.driver.find_element(By.CSS_SELECTOR, "button.action.primary.checkout")
        click_report(place_order_btn,"Place Order Button")
        print('Successfully Placed Order')

    def print_order(self):
        wait_until_url(self.driver, "success")
        span_text = self.driver.find_element(By.CSS_SELECTOR,"#maincontent > div.page-title-wrapper > h1 > span").text
        print("Website Message: ", span_text)
        end_btn = self.driver.find_element(By.CSS_SELECTOR,"#maincontent > div.columns > div > div.checkout-success > div > div > a")
        click_report(end_btn,"Back To Main Page Button")