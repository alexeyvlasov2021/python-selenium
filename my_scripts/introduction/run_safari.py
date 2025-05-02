from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Safari()
driver.implicitly_wait(15)

driver.get("https://itc.ua/ua/")

# consent is not showing up on this browser
# consent_btn = driver.find_element(By.XPATH, '//button[@aria-label="Consent"]')
accept_btn = driver.find_element(By.ID, 'cookie-accept')

# consent_btn.click()
accept_btn.click()

# option 1 how to keep Safari opened
input("Press Enter to exit and close browser...")

# option 2
# time.sleep(9999)  # Keeps it open for a long time

# driver.quit()