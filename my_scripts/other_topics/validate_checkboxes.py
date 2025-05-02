import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("http://127.0.0.1:5500/index.html")

# validate total number of checkboxes

# expected_count_of_checkboxes = 3

all_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# actual_count = len(all_checkboxes)
# message = f"expected checkboxes count should be {expected_count_of_checkboxes}"

# assert actual_count == expected_count_of_checkboxes, message
# assert actual_count == expected_count_of_checkboxes, f"expected checkboxes count should be {expected_count_of_checkboxes}"

count = 0
try:

    for cb in all_checkboxes:
        element = wait.until(expected_conditions.element_to_be_clickable(cb))
        print(f"element {count} is clickable")
        count+=1

    print("all elements are clickable")

except:
    print( f"element {count} is not clickable")

