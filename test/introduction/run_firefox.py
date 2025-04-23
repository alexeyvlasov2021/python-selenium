from selenium.webdriver.common.by import By
# alternative webdriver
# from selenium.webdriver.firefox import webdriver
from selenium import webdriver

# alternative webdriver
# driver = webdriver.WebDriver()
driver = webdriver.Firefox()
driver.implicitly_wait(15)

driver.get("https://itc.ua/ua/")

consent_btn = driver.find_element(By.XPATH, '//button[@aria-label="Consent"]')
accept_btn = driver.find_element(By.ID, 'cookie-accept')

consent_btn.click()
accept_btn.click()

# driver.quit()