from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utils import fill_textbox, click_report, wait_until_visible, wait_until_url


class Cart:
    def __init__(self, driver):
        self.driver = driver


    def delete_item(self):
        wait_until_visible(self.driver,By.XPATH, "//*[@id='shopping-cart-table']/tbody[2]/tr[2]/td/div/a[3]")
        delete_item_btn = self.driver.find_element(By.XPATH, "//*[@id='shopping-cart-table']/tbody[2]/tr[2]/td/div/a[3]")
        click_report(delete_item_btn, "Delete Bottom From Shopping Cart")
        print('Successfully Deleted Bottom From Cart')


    def edit_item(self):
        # Wait until the item's Edit button is visible, then click it
        wait_until_visible(self.driver,By.LINK_TEXT, "Edit")
        edit_btn = self.driver.find_elements(By.LINK_TEXT,"Edit")[0]
        click_report(edit_btn, "Edit")

        # Size and color options load last, so wait for them to fully appear before attempting to change the quantity
        wait_until_url(self.driver,"product_id/")
        wait_until_visible(self.driver, By.ID,"option-label-size-143")

        # Size and color selections may reset even if they were previously selected. Make sure both are selected again;
        # if not, choose each option to enable the 'Update to Cart' button
        size_s = self.driver.find_element(By.ID,"option-label-size-143-item-167")
        color_blue = self.driver.find_element(By.ID,"option-label-color-93-item-50")
        if size_s.get_attribute("aria-checked") == "false":
            click_report(size_s, "Edit Size S")

        if color_blue.get_attribute("aria-checked") == "false":
            click_report(color_blue, "Edit Color Blue")

        # Finally, change the quantity
        fill_textbox(self.driver, "qty", 4,"Quantity")
        update_btn = self.driver.find_element(By.ID,"product-updatecart-button")
        click_report(update_btn, "Update To Cart")
        print('Successfully Updated Quantity to Four Tops In Cart')


    def fill_summary_info(self):
        # Open summery block
        title_element = self.driver.find_element( By.CSS_SELECTOR,"div.title[data-role='title'][aria-controls='block-summary']" )
        click_report(title_element, "Open Summary Info")

        # Wait for all items to load before filling in the information
        wait_until_visible(self.driver,By.NAME,"country_id")
        county_btn  = self.driver.find_element(By.NAME,"country_id")
        select = Select(county_btn)
        select.select_by_visible_text("Israel")
        wait_until_visible(self.driver, By.NAME, "region")
        fill_textbox(self.driver, "region", 'Israel', "",By.NAME)
        wait_until_visible(self.driver, By.NAME, "postcode")
        fill_textbox(self.driver, "postcode", '4960045', "",By.NAME)
        proc_to_checkout_btn = self.driver.find_element(By.XPATH,"//*[@id='maincontent']/div[3]/div/div[2]/div[1]/ul/li[1]/button")
        click_report(proc_to_checkout_btn, "Proceed To Checkout")
        print('Successfully Filled Summary Info')

