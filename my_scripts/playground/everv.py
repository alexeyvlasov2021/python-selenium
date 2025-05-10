import os
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# before script run, chrome with this profile should be closed
# the corrected path to folder where located user profiles on Mac. you cannot just paste path
user_data_dir = os.path.expanduser('~/Library/Application Support/Google/Chrome')
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(chrome_options)
driver.get("https://everve.cc/")
wait = WebDriverWait(driver, 5)
driver.maximize_window()

# skipping exception or clicking button
try:
    accept_cookies_btn = wait.until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//button[text() = 'Alle akzeptieren']")))
    accept_cookies_btn.click()
except TimeoutException:
    # print("no accept cookie button is displayed")
    pass


mans_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "li#mega-menu-item-234514>a")))
mans_btn.click()

ezero_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "li#mega-menu-item-everve-subnavi-image-20>a")))
ezero_btn.click()

first_product = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a.woocommerce-LoopProduct-link")))
first_product.click()

crazy_btn = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Wähle deinen')]")))
crazy_btn.click()

configure_btn = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='konfigurieren']")))
configure_btn.click()

rennrad_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "label[for='rennrad']")))
rennrad_btn.click()


