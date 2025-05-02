from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# https://stackoverflow.com/questions/76614392/getting-error-when-i-run-selenium-script-value-error-timeout-value-connect-was
# required the downgrade of urllib
# pip install --upgrade urllib3==1.26.16

# working version
# selenium==3.141.0
# urllib3==1.26.16


# worked when specify path to the latest chromedriver
# driver = webdriver.Chrome("/Users/alexeyvlasov/Downloads/chromedriver-mac-arm64/chromedriver")
# works fine if driver file is added to the bin folder of my venv
driver = webdriver.Chrome()
driver.implicitly_wait(15)

driver.get("https://itc.ua/ua/")

btn_1 = driver.find_element_by_css_selector("button[aria-label='Consent']")
btn_1.click()