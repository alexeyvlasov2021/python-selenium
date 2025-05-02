from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://www.formula1.com/")

# wait for a frame and switch to it
wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.ID, "sp_message_iframe_1149950")))

accept_btn = driver.find_element(By.CSS_SELECTOR, 'button[title="ACCEPT ALL"]')
accept_btn.click()

# switching back
driver.switch_to.default_content()
results_link = driver.find_element(By.CSS_SELECTOR, "a[href='https://www.formula1.com/en/results/2025/races']")
results_link.click()
