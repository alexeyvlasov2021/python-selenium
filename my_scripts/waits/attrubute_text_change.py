import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("http://127.0.0.1:5500/index.html")
driver.maximize_window()

wait = WebDriverWait(driver, timeout= 10)

wait.until(expected_conditions.text_to_be_present_in_element_attribute((By.TAG_NAME, "p"), "title", "Super man"))
print("attribute text change")