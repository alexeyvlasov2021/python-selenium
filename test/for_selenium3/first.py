from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(15)

driver.get("https://itc.ua/ua/")

btn_1 = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Consent']")
btn_1.click()