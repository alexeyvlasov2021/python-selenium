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

driver.get("http://127.0.0.1:5500/index.html")

time.sleep(5)

one_chbx = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'One')]/input")))
two_chbx = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Two')]/input")))
three_chbx = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Three')]/input")))
four_chbx = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Four')]/input")))

one_chbx.click()
four_chbx.click()
three_chbx.click()

# check if checkbox is selected
print("four checkbox is checked: {}".format(four_chbx.is_selected()))