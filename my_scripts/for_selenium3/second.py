from selenium import webdriver


# did not work when I specify path to the latest geckofriver in Firfox()
# works fine if driver file is added to the bin folder of my venv
driver = webdriver.Firefox()
driver.implicitly_wait(15)

driver.get("https://itc.ua/ua/")

btn_1 = driver.find_element_by_css_selector("button[aria-label='Consent']")
btn_1.click()