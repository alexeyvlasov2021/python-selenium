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

driver.get("http://127.0.0.1:5500/index.html")
time.sleep(3)

# call alert message
simple_alert_call_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'button:nth-of-type(1)')))
simple_alert_call_btn.click()

# return alert node and switch to it
my_alert = driver.switch_to.alert
time.sleep(2)
# accept
my_alert.accept()

# call alert message
call_confirm_alert_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'button:nth-of-type(2)')))
call_confirm_alert_btn.click()


# return alert node and switch to it
my_confirm_alert = driver.switch_to.alert
time.sleep(2)
# cancel
my_confirm_alert.dismiss()
