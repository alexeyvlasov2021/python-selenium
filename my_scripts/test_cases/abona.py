from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)
wait = WebDriverWait(driver, timeout=2)

driver.get('https://www.abona-erp.com/')
driver.maximize_window()

reject_all_btn = wait.until(expected_conditions.element_to_be_clickable((By.ID, "ppms_cm_reject-all")))
reject_all_btn.click()