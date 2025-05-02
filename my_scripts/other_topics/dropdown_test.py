import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("http://127.0.0.1:5500/index.html")
time.sleep(2)

img_btn = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "img")))
img_btn.click()

link2 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='nav']/a[2]")))
link2.click()
time.sleep(2)
driver.back()

# list = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'cars')))
# list.click()

select_element = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'cars')))
select = Select(select_element)
# get list of options
option_list = select.options
print(option_list)

time.sleep(2)
# select by visible text
select.select_by_visible_text('Saab')
time.sleep(2)
# select by value
select.select_by_value('audi')
time.sleep(2)
# select by index
select.select_by_index(0)
time.sleep(2)

# exception thrown when selected disabled option
# select.select_by_visible_text('ddd')


select_element2 = wait.until(expected_conditions.element_to_be_clickable((By.NAME, 'multi')))
select2 = Select(select_element2)
select2.select_by_visible_text('Ham')
time.sleep(2)
select2.select_by_visible_text('Sausages')
time.sleep(2)
select2.deselect_by_visible_text('Ham')

# exception - you cannot deselect non multiselect list
# time.sleep(2)
# select.deselect_by_index(0)

time.sleep(2)
driver.quit()

