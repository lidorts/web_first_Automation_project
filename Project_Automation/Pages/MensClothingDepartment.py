from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utils import click_report, wait_until_visible


class MensClothingDepartment:
    def __init__(self, driver):
        self.driver = driver


    def navigate_to_men_clothing(self):
        men_btn = self.driver.find_element(By.ID, "ui-id-5")
        click_report(men_btn, "Men's Clothing Department Page Button")


    def choose_category_top(self):
        top_btn = self.driver.find_element(By.LINK_TEXT, "Tops")
        click_report(top_btn, "Tops category")

        # Filter the results and sort items by the lowest price
        position_dropdown = self.driver.find_element(By.ID, "sorter")
        select = Select(position_dropdown)
        select.select_by_visible_text("Price")
        print('Sorting By - Price')


    def add_tops(self):
        wait_until_visible(self.driver, By.LINK_TEXT,"Cassius Sparring Tank")
        add_shirt = self.driver.find_element(By.LINK_TEXT,"Cassius Sparring Tank")
        click_report(add_shirt, "Shirt")

        choose_size = self.driver.find_element(By.ID, "option-label-size-143-item-167")
        click_report(choose_size, "Size M")

        choose_color = self.driver.find_element(By.ID, "option-label-color-93-item-50")
        click_report(choose_color, "Selected Color Blue")

        add_to_cart = self.driver.find_element(By.ID, "product-addtocart-button")
        click_report(add_to_cart, "Add To Cart")

        print('Successfully Added Top To Cart')

        go_back = self.driver.find_element(By.LINK_TEXT, "Men")
        click_report(go_back, "Return To Men's Clothing Department Page Button")


    def choose_category_bottom(self):
        bottom_btn = self.driver.find_element(By.LINK_TEXT, "Bottoms")
        click_report(bottom_btn, "Bottoms category")

        # Filter the results and sort items by the lowest price
        position_dropdown = self.driver.find_element(By.ID, "sorter")
        select = Select(position_dropdown)
        select.select_by_visible_text("Price")
        print('Sorting By - Price')


    def add_bottoms(self):
        add_pants = self.driver.find_element(By.LINK_TEXT, "Arcadio Gym Short")
        click_report(add_pants, "Pants")

        choose_size = self.driver.find_element(By.ID, "option-label-size-143-item-176")
        click_report(choose_size, "Size 33")

        choose_color = self.driver.find_element(By.ID, "option-label-color-93-item-50")
        click_report(choose_color, "Selected Color Blue")

        add_to_cart = self.driver.find_element(By.ID, "product-addtocart-button")
        click_report(add_to_cart, "Add To Cart")
        print('Successfully Added Bottom To Cart')


    def choose_category_jacket(self):
        self.driver.find_element(By.ID, "ui-id-5").click()
        jacket_btn = self.driver.find_element(By.LINK_TEXT,"Jackets")
        click_report(jacket_btn, "Jacket Category Page Button")


    def add_jacket(self):
        add_jacket = self.driver.find_element(By.LINK_TEXT, "Lando Gym Jacket")
        click_report(add_jacket, "Jacket")

        choose_size = self.driver.find_element(By.ID, "option-label-size-143-item-169")
        click_report(choose_size, "Size L")

        choose_color = self.driver.find_element(By.ID, "option-label-color-93-item-52")
        click_report(choose_color, "Selected Color Gray")

        add_to_cart = self.driver.find_element(By.ID, "product-addtocart-button")
        click_report(add_to_cart, "Add To Cart")
        print('Successfully Added Jacket To Cart')

