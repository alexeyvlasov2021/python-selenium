from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#options needed to keep browser opened after script is executed
options = Options()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options)
driver.implicitly_wait(15)

driver.get("https://itc.ua/ua/")

consent_btn = driver.find_element(By.XPATH, '//button[@aria-label="Consent"]')
accept_btn = driver.find_element(By.ID, 'cookie-accept')

consent_btn.click()
accept_btn.click()

driver.quit()
