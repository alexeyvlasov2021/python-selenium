import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
# driver = webdriver.Firefox()
# driver = webdriver.Safari()
driver.maximize_window()

wait = WebDriverWait(driver, 5)

driver.get("http://127.0.0.1:5500/")
time.sleep(3)

# this demo is based on Udemy lecture and slightly different approach to access 'alert' elements
my_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'button')))
# trigger prompt message
my_btn.click()
time.sleep(2)
# switch to and assign prompt (alert) element
prompt_alert = driver.switch_to.alert
# type text into prompt window
prompt_alert.send_keys("Alexey (Oleksii) Vlasov")
# accept prompt
prompt_alert.accept()

# trigger prompt message
my_btn.click()
time.sleep(2)
prompt_alert = driver.switch_to.alert
# type text into prompt window
prompt_alert.send_keys("any text")
# cancel prompt
prompt_alert.dismiss()