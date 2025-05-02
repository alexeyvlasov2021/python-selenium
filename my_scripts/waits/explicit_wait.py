import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("http://127.0.0.1:5500/index.html")
driver.maximize_window()

wait = WebDriverWait(driver, timeout= 10)

h1 = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "h1")))
driver.execute_script("arguments[0].style.color = 'red'", h1)

def do_stuff():
    time.sleep(2)
    driver.switch_to.new_window('tab')
#     same if used 'window'

windows_before = driver.window_handles

do_stuff()

# wait.until(expected_conditions.new_window_is_opened(windows_before))
wait.until(expected_conditions.number_of_windows_to_be(2))

print("wait is passed")