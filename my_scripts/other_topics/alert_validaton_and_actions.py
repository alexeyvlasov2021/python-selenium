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
driver.maximize_window()

wait = WebDriverWait(driver, 5)
driver.get("http://127.0.0.1:5500/index.html")

alert_btn = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text() = "show alert"]')))
confirm_btn = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text() = "show confirm"]')))

# handle alert

# initiate alert
alert_btn.click()
time.sleep(3)
# wait for alert
alert = wait.until(lambda d: d.switch_to.alert)
# get alert text
text = alert.text
print(f"your alert text is: '{text}'")
# accept or close alert window
alert.accept()

# handle confirm
# initiate alert
confirm_btn.click()
time.sleep(3)
confirm_msg = wait.until(lambda d: d.switch_to.alert)
confirm_text = confirm_msg.text
print(f"this is your confirm message text: '{confirm_text}'")
# dismiss message
confirm_msg.dismiss()

confirm_btn.click()
time.sleep(3)
confirm_msg2 = wait.until(lambda d: d.switch_to.alert)
# accept message
confirm_msg2.accept()