import random
import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

from Project_Automation.Pages.Cartpage import Cart
from Project_Automation.Pages.CheckOutPage import Checkout
from Project_Automation.Pages.LoginPage import Login
from Project_Automation.Pages.MensClothingDepartment import MensClothingDepartment
from Project_Automation.Pages.RegistrationPage import Registration


class ProjectAutomation(unittest.TestCase):
    # Use a random number to make each email address different per execution
    num_for_mail = random.randint(1, 1000)
    user_mail = f'gill_shalev{num_for_mail}@gmail.com'
    password = 'Gillshalev123456789'

    @classmethod
    def setUpClass(cls):
        print("\nSetUpClass")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()


    def setUp(self):
        print("SetUp")


    def test1_Registration(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        print("                                     Test 1 - Registration")
        registration = Registration(driver)
        registration.navigate_to_create_an_account()
        registration.fill_account_info(self.user_mail, self.password)
        registration.sign_out()
        time.sleep(1)
        print("***** The Registration Test Has Been Successfully Completed *****")
        time.sleep(1)


    def test2_log_in(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        print("                                     Test 2 - Log In")
        login = Login(driver)
        login.navigate_to_login()
        login.fill_saved_account_info(self.user_mail, self.password)
        print("***** The Login Test Has Been Successfully Completed *****")
        time.sleep(1)


    def test3_add_items(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        print("                                     Test 3 - Add Items To Cart")
        add_men_items = MensClothingDepartment(driver)
        add_men_items.navigate_to_men_clothing()
        add_men_items.choose_category_top()
        add_men_items.add_tops()
        add_men_items.choose_category_bottom()
        add_men_items.add_bottoms()
        add_men_items.choose_category_jacket()
        add_men_items.add_jacket()
        print("***** The Adding Items To Cart Test Has Been Successfully Completed *****")
        time.sleep(2)

    def test4_cart_editing(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/checkout/cart/")
        print("                                     Test 4 - Edit Cart")
        cart_edit = Cart(driver)
        #cart_edit.navigate_to_cart()
        cart_edit.change_qty()
        cart_edit.fill_summary_info()
        print("***** The Cart Editing Test Has Been Successfully Completed *****")
        time.sleep(1)
       

    def test5_checkout(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/checkout/#shipping")
        print("                                     Test 5 - Checkout")
        checkout = Checkout(driver)
        checkout.fill_checkout_info()
        checkout.place_order()
        checkout.print_order()
        print("***** The Checkout Test Has Been Successfully Completed *****")
        time.sleep(2)


    def tearDown(self):
        print("tearDown")


    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        cls.driver.close()