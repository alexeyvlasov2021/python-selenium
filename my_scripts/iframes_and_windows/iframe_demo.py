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

show_btn = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text() = 'show frame']")))
show_btn.click()
time.sleep(2)

# this alert called when iframe is loaded
# no need to switch to iframe first! - exception occurs 'unexpected alert open: {Alert text : inside iframe alert}'
my_alert1 =  driver.switch_to.alert
print(f"first alert text is: {my_alert1.text}")
my_alert1.accept()

# locate iframe
my_frame = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'iframe')))
# switch to iframe
# driver.switch_to.frame(my_frame)

# first iframe index starts from 0
# driver.switch_to.frame(0)

# iframe id or name
driver.switch_to.frame('iframe_name')
time.sleep(2)

show_alert_btn = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text() = 'show']")))
show_alert_btn.click()

# this alert is called after button click inside the iframe
my_alert =  driver.switch_to.alert
print(f"second alert text is: {my_alert.text}")
my_alert.accept()

# as I understand, there is no need to switch back to iframe
close_btn = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text() = 'close']")))
time.sleep(2)
close_btn.click()

driver.switch_to.default_content()
time.sleep(2)
# there is no need to assign below variable once again
# show_btn = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text() = 'show frame']")))

# screenshot throws exception if alert is not closed
# driver.save_screenshot('./image.png')
show_btn.click()
time.sleep(2)
driver.quit()