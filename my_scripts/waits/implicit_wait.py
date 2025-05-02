from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

# driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5500/index.html")

driver.maximize_window()
driver.implicitly_wait(15)

h1 = driver.find_element(By.CSS_SELECTOR, "h1")
driver.execute_script("arguments[0].style.color = 'red'", h1)