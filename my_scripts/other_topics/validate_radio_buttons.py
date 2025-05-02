import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 5)

driver.get("http://127.0.0.1:5500/index.html")

# validate what radio button is default
expected_value = 'mail'
# actual_value = ''


# method 1
# try:
#     # is a list of WebElements
#     radio_buttons = wait.until(
#         expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input[name="contact"]')))
#
#     for btn in radio_buttons:
#         # value could be 'true' on ''
#         is_checked = btn.get_attribute("checked")
#         if is_checked:
#             # read button value attribute and assign it to the variable
#             actual_value = btn.get_attribute("value")
#     # AssertionError is an exception
#     assert expected_value == actual_value, f"wrong actual result: '{actual_value}'. expected: '{expected_value}'"
#     print("proper radio button is set as default")
#
# # here intercepted only timeout error if one of elements is invisible
# except TimeoutException:
#     print("one of radio buttons is not visible")

# method 2 - better way to check default selection
default_selected_element = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, f'input[name="contact"][value="{expected_value}"]')))

assert default_selected_element.is_selected(), f"the expected element ('{expected_value}') is not default"

# check if all value present
radio_values = ['email', 'phone', 'mail']
radio_btns = wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[name="contact"]')))

# for i in range(len(radio_values)):
#     current_value = radio_btns[i].get_attribute('value')
#     assert current_value in radio_values, f"this value '{current_value}' is out of the list"

for rb in radio_btns:
    current_value = rb.get_attribute('value')
    assert current_value in radio_values, f"this value '{current_value}' is out of the list"


print("all values are on the page")