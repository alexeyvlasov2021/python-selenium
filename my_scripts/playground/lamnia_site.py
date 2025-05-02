#options needed to keep browser opened after script is executed
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.implicitly_wait(120)


driver.get("https://www.lamnia.com/ru")

menu_btn = driver.find_element(By.CSS_SELECTOR, "span[data-target='navigation-category-container']")
soon_in_sales_lnk = driver.find_element(By.XPATH, "//a[contains(text(), 'Скоро в продаже')]")

ActionChains(driver) \
       .move_to_element(menu_btn) \
       .pause(3) \
       .move_by_offset(-100, -100) \
       .move_to_element(soon_in_sales_lnk) \
       .perform()

search_fld = driver.find_element(By.ID, "searchbox")
search_submit_btn = driver.find_element(By.ID, "sidebar-search-submit")

search_fld.send_keys("microtech")
search_submit_btn.click()

acc_cookie = driver.find_element(By.ID, "cookie_all")
acc_cookie.click()

close_dialog_btn = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Close dialog']")
close_dialog_btn.click()
