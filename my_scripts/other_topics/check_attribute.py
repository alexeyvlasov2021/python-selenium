import time
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

driver.get("http://demostore.supersqa.com/")

search_fld = driver.find_element(By.ID, "woocommerce-product-search-field-0")

# two ways how to get element attribute value
# placeholder = driver.execute_script("return arguments[0].getAttribute('placeholder')", search_fld)
placeholder = search_fld.get_attribute("placeholder")

print("your attribute is \"{}\"".format(placeholder))

search_fld.send_keys("Alexey Vlasov")
value = search_fld.get_attribute("value")

print("your value is \"{}\"".format(value))
