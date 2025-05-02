import time
from selenium import webdriver
from selenium.webdriver import Keys
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
# time.sleep(1)

# wait for input text field to be ready for data input
search_fld = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'woocommerce-product-search-field-0')))
# typing a text in the field
search_fld.send_keys('Alexey')
# wait for value is changed for the input field
wait.until(expected_conditions.text_to_be_present_in_element_attribute((By.ID, 'woocommerce-product-search-field-0'), 'value', 'Alexey'))
# get its value and print it
input_text =  search_fld.get_attribute('value')
print('your \"value\" is: {}'.format(input_text))
# hit enter key to submit search
search_fld.send_keys(Keys.ENTER)

page_title = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "h1.page-title")))
print('title text is: {}'.format(page_title.text))