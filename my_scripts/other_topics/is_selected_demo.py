import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get('http://127.0.0.1:5500/index.html')

volvo_option = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//option[text() = "Volvo"]')))
saab_option = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//option[text() = "Saab"]')))
dropdown_list = wait.until(expected_conditions.element_to_be_clickable((By.ID, "cars")))

dp_select = Select(dropdown_list)

# shows selected option
print('volvo is selected: {}'.format(volvo_option.is_selected()))
print('saab is selected: {}'.format(saab_option.is_selected()))

# not applicable to input text field
dp_select.select_by_visible_text("Saab")

# shows selected option
print("==============================")
print('volvo is selected: {}'.format(volvo_option.is_selected()))
print('saab is selected: {}'.format(saab_option.is_selected()))

name_input = wait.until(expected_conditions.element_to_be_clickable((By.ID, "name")))
print("==============================")
print("name input is selected: {}".format(name_input.is_selected()))

name_input.send_keys("a")
print("==============================")
print("name input is selected: {}".format(name_input.is_selected()))

name_input.click()
print("==============================")
print("name input is selected: {}".format(name_input.is_selected()))
