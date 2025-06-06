from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


from Project_Automation.Utils import navigate_link_text, fill_textbox, click_report, wait_until_visible


class Cart:
    def __init__(self, driver):
        self.driver = driver


    def change_qty(self):
        delete_item_btn = self.driver.find_element(By.XPATH,"//*[@id='shopping-cart-table']/tbody[2]/tr[2]/td/div/a[3]")
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", delete_item_btn)
        click_report(delete_item_btn, "Delete Bottom From Shopping Cart")
        print('Successfully Deleted Bottom From Cart')
        wait_until_visible(self.driver,By.LINK_TEXT, "Edit")
        edit_btn = self.driver.find_elements(By.LINK_TEXT,"Edit")[0]
        click_report(edit_btn, "Edit")
        fill_textbox(self.driver, "qty", 4,"Quantity")
        # wait_until_visible(self.driver,By.ID,"option-label-color-93-item-50")
        # self.driver.find_element(By.ID,"option-label-color-93-item-50").click()
        update_btn = self.driver.find_element(By.ID,"product-updatecart-button")
        click_report(update_btn, "Update To Cart")
        print('Successfully Updated Quantity to Four Tops In Cart')





    def fill_summary_info(self):
        title_element = self.driver.find_element( By.CSS_SELECTOR,"div.title[data-role='title'][aria-controls='block-summary']" )
        click_report(title_element, "Open Summary Info")
        print('Successfully Filled Summary Info')


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


