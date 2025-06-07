from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utils import (fill_textbox, click_report, wait_until_visible, wait_until_url
, wait_until_invisible)


class Checkout:
    def __init__(self, driver):
        self.driver = driver


    def fill_checkout_info(self):
        # Wait for all items to load before filling in the information.
        wait_until_url(self.driver, "#shipping")
        wait_until_visible(self.driver,By.NAME,"company")
        fill_textbox(self.driver,"company",'John Bryce', "",By.NAME)
        wait_until_visible(self.driver, By.NAME, "street[0]")
        fill_textbox(self.driver, "street[0]", 'Jabotinsky Street', "",By.NAME)
        wait_until_visible(self.driver, By.NAME, "street[1]")
        fill_textbox(self.driver, "street[1]", '3-rd floor, apartment 12', "",By.NAME)
        wait_until_visible(self.driver, By.NAME, "city")
        fill_textbox(self.driver, "city", 'Petah-Tikva', "",By.NAME)
        wait_until_visible(self.driver, By.NAME, "postcode")
        fill_textbox(self.driver, "postcode", '4960045', "",By.NAME)

        # Fill information in countries Drop-Down
        county_checkout_btn = self.driver.find_element(By.NAME, "country_id")
        select = Select(county_checkout_btn)
        select.select_by_visible_text("Israel")

        fill_textbox(self.driver, "telephone", '054-2330398', "",By.NAME)
        wait_until_visible(self.driver,By.XPATH, "//*[@id='shipping-method-buttons-container']/div/button")
        next_btn = self.driver.find_element(By.XPATH,"//*[@id='shipping-method-buttons-container']/div/button")
        click_report(next_btn,"Next Button")
        print('Successfully Filled Checkout Info')


    def place_order(self):
        # During checkout, it seems the website loads all elements but has a loading mask over it
        # so we wait until the url is loaded and the loading mask disappears
        wait_until_url(self.driver,"#payment")
        wait_until_invisible(self.driver, By.CSS_SELECTOR, ".loading-mask")

        # Click on check out button
        wait_until_visible(self.driver, By.CSS_SELECTOR, "button.action.primary.checkout")
        place_order_btn = self.driver.find_element(By.CSS_SELECTOR, "button.action.primary.checkout")
        click_report(place_order_btn,"Place Order Button")
        print('Successfully Placed Order')


    def print_order_and_return_to_main(self):
        # Wait for the order to complete and navigate to 'success' page
        wait_until_url(self.driver, "success")

        # Get success message
        span_text = self.driver.find_element(By.CSS_SELECTOR,"#maincontent > div.page-title-wrapper > h1 > span").text
        print("Website Message: ", span_text)

        # Navigate back to main menu
        end_btn = self.driver.find_element(By.CSS_SELECTOR,"#maincontent > div.columns > div > div.checkout-success > div > div > a")
        click_report(end_btn,"Back To Main Page Button")

