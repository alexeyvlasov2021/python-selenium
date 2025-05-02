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
items_count = driver.find_element(By.XPATH, "//*[@id='site-header-cart']/descendant::span[@class  = 'count']")
items_count_value = int(items_count.text.split(" ")[0])

# print(type(items_count_value)) #<class 'int'>
print("current count value is: {}".format(items_count_value))