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

my_btn = wait.until(expected_conditions.element_to_be_clickable((By.TAG_NAME, 'button')))

# first attempt - accept prompt
my_btn.click()
time.sleep(2)
alert = wait.until(lambda d: d.switch_to.alert)
alert.send_keys("Hanna Vlasova")
time.sleep(2)
# text = alert.text
# print(f"alert text is: {text}")
# time.sleep(2)
alert.accept()
#
# # second attempt - decline prompt
# my_btn.click()
# time.sleep(2)
# alert = wait.until(lambda d: d.switch_to.alert)
# alert.send_keys("Oleksii Vlasov")
# time.sleep(2)
# text = alert.text
# time.sleep(2)
# alert.dismiss()