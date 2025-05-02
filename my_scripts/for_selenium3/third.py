import time

from selenium import webdriver

driver = webdriver.Safari()
driver.implicitly_wait(15)

driver.get("https://itc.ua/ua/")

# btn_1 = driver.find_element_by_css_selector("button[aria-label='Consent']")
# btn_1.click()

time.sleep(3)
driver.quit()