import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

driver.get("https://itc.ua/")
driver.implicitly_wait(10)

cons_btn = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Consent']")
acc_btn = driver.find_element(By.ID, "cookie-accept")
login_btn = driver.find_element(By.XPATH, "(//a[text()='Увійти'])[2]")

cons_btn.click()
acc_btn.click()
login_btn.click()

# login page
remember_chb = driver.find_element(By.ID, "remember_me")
h3 = driver.find_element(By.XPATH, "//h3[text()='Увійти']")
# cannot click element, it is overlapped
# remember_chb.click()

# this how execute script
driver.execute_script("arguments[0].click();",remember_chb)
time.sleep(5)
driver.execute_script("arguments[0].style.color = 'red'", h3)
driver.execute_script("arguments[0].style.fontSize = '5rem'", h3)


