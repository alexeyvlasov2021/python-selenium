import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_open_itc_site_with_pytest():
    # options needed to keep browser opened after script is executed
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get("https://itc.ua/")
    time.sleep(2)
    driver.quit()