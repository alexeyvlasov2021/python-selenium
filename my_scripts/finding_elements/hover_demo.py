import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.implicitly_wait(15)


driver.get("http://127.0.0.1:5500/index.html")

hoverable = driver.find_element(By.TAG_NAME, "button")

time.sleep(2)

ActionChains(driver) \
        .move_to_element(hoverable) \
        .pause(3) \
        .move_by_offset(200, 200) \
        .perform()

# open new window
driver.switch_to.new_window('window')

# open new tab
# driver.switch_to.new_window('tab')
driver.get("https://itc.ua/ua/")

ids = driver.window_handles
driver.switch_to.window(ids[0])

