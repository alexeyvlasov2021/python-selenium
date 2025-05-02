import time

from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def run_script():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options)
    driver.get("http://demostore.supersqa.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # home page
    my_account_lnk = driver.find_element(By.CSS_SELECTOR, "ul[class='nav-menu'] li[class='page_item page-item-9'] a")
    my_account_lnk.click()

    # my account page
    eml_fld = driver.find_element(By.XPATH, "//input[@id='username']")
    psw_fld = driver.find_element(By.XPATH, "//input[@id='password']")
    remb_cbx = driver.find_element(By.XPATH, "//input[@id='rememberme']")
    log_in_btn = driver.find_element(By.XPATH, "//button[@name='login']")

    eml_fld.send_keys("alexey@gmail.com")
    psw_fld.send_keys("123456")
    remb_cbx.click()
    log_in_btn.click()

    msg_txt = driver.find_element(By.XPATH, "//div[@id='content']//li[1]")
    err_txt1 = "Unknown email address. Check again or try your username."

    assert msg_txt.text == err_txt1
    # print error text

    print(msg_txt.text)

    # refresh elements locator to fix stale error
    eml_fld = driver.find_element(By.XPATH, "//input[@id='username']")
    log_in_btn = driver.find_element(By.XPATH, "//button[@name='login']")

    eml_fld.clear()
    log_in_btn.click()

    # print error text
    # need sleep to avoid data hasn't been refreshed
    time.sleep(1)
    msg_txt = driver.find_element(By.XPATH, "//div[@id='content']//li[1]")
    err_txt2 = "Error: Username is required."

    assert msg_txt.text == err_txt2
    print(msg_txt.text)

    driver.quit()


for i in range(1, 2):
    print("-------------------- run=#{}". format(i))
    run_script()



