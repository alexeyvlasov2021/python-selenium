import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("http://demostore.supersqa.com/")

# method 1
def get_active_tab():
    tabs_items = driver.find_elements(By.XPATH, "//ul[@class='nav-menu']/li")
    for tab in tabs_items:
        tab_class = tab.get_attribute('class')

        # check substring in string
        if "current_page_item" in tab_class:
            print("active tab is: \"{}\"".format(tab.text))


simple_page_lnk = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Sample Page")))
# you can read inner text even if selected element (node) has child
# print(simple_page_lnk.text)
simple_page_lnk.click()

get_active_tab()

checkout_lnk = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'page_item')]/a[contains(text(), 'Checkout')]")))
checkout_lnk.click()

get_active_tab()

# method 2

# my_tab = driver.find_element(By.XPATH, '//li[contains(@class, "current_page_item")]/ a')
# print("selected tab: \"{}\"".format(my_tab.text))
#
# my_acc_lnk = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "My account")))
# my_acc_lnk.click()
#
# my_tab = driver.find_element(By.XPATH, '//li[contains(@class, "current_page_item")]/ a')
# print("selected tab: \"{}\"".format(my_tab.text))

