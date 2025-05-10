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

# to close bootstrap alert you need to click its link
close_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'a.close')))
close_btn.click()