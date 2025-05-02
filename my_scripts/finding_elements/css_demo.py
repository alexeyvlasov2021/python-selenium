from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.implicitly_wait(15)


driver.get("http://demostore.supersqa.com/")

# main page
cart_lnk = driver.find_element(By.CSS_SELECTOR, "ul#site-header-cart>li>a.cart-contents")
cart_lnk.click()

# cart page
return_lnk = driver.find_element(By.CSS_SELECTOR, "a.button.wc-backward")
return_lnk.click()

# main page
my_account_lnk = driver.find_element(By.CSS_SELECTOR, "ul.nav-menu > li:nth-child(4) >a")
page_lnk = driver.find_element(By.CSS_SELECTOR, "a.page-numbers:nth-of-type(1)")

# my_account_lnk.click()
page_lnk.click()

# page 2
page_lnk = driver.find_element(By.CSS_SELECTOR, "ul.page-numbers li:nth-child(2) a")
page_lnk.click()
