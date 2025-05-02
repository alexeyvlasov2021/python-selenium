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

driver.get("http://127.0.0.1:5500/")
time.sleep(1)

folding_radio = driver.find_element(By.ID, "folding")
folding_radio.click()

cold_steel_chbx = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'cold_steel')))
zero_tolerance_chbx = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'zero_tolerance')))

time.sleep(1)
cold_steel_chbx.click()
zero_tolerance_chbx.click()

time.sleep(1)
fixed_radio = driver.find_element(By.ID, "fixed")
fixed_radio.click()

miyabi_chbx = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'miyabi')))
time.sleep(1)
miyabi_chbx.click()

time.sleep(1)
driver.quit()