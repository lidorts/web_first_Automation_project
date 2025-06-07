from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def navigate_link_text(driver, text):
    element = driver.find_element(By.LINK_TEXT, text)
    click_report(element, text)


def click_report(element,name):
    element.click()
    print("Clicking on: " + name)


def fill_textbox(driver, element_id, content,  textbox_name = "" ,find_by = By.ID):
    element = driver.find_element(find_by, element_id)
    element.clear()
    element.send_keys(content)

    # Print 'element id' as 'text box name' when 'text box name' is not provided
    if textbox_name == "":
        textbox_name = element_id
    print(f"Filling Textbox {textbox_name}: {content}")


def wait_until_visible(driver, find_by, element_to_find):
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((find_by, element_to_find)))


def wait_until_url(driver,url_part):
    WebDriverWait(driver, 10).until(ec.url_contains(url_part))


def wait_until_invisible(driver, find_by, element_to_find):
    WebDriverWait(driver, 10).until(ec.invisibility_of_element_located((find_by, element_to_find)))