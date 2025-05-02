from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.implicitly_wait(15)


driver.get("https://www.formula1.com/")

# how to switch to iframe and back
# https://www.browserstack.com/guide/handling-frames-in-selenium#:~:text=Another%20way%20to%20switch%20between,it%20to%20the%20switch%20method.
# my_frame = driver.find_element(By.ID, "sp_message_iframe_1149950")
# driver.switch_to.frame(my_frame)

# we can use also frame index
driver.switch_to.frame(0)
acc_btn = driver.find_element(By.XPATH, "//*[@id='notice']/div[3]/button[2]")
acc_btn.click()

# switching back
driver.switch_to.default_content()
results_link = driver.find_element(By.CSS_SELECTOR, "a[href='https://www.formula1.com/en/results/2025/races']")
results_link.click()

# my_frame = driver.find_element(By.ID, "sp_message_iframe_1149950")
# driver.switch_to.frame(my_frame)

# we can also use string as iframe name or iframe id
driver.switch_to.frame("sp_message_iframe_1149950")
acc_btn = driver.find_element(By.XPATH, "//*[@id='notice']/div[3]/button[2]")
acc_btn.click()

driver.switch_to.default_content()
drivers_link = driver.find_element(By.XPATH, '//a[text()="Drivers" and @class="block"]')
drivers_link.click()

gaming = driver.find_element(By.XPATH, '//*[@id="Gaming"]')
ActionChains(driver).click_and_hold(gaming).perform()

f1_clash_lnk = driver.find_element(By.XPATH, '//a[contains(text(), "F1 Clash")]')
f1_clash_lnk.click()

# clash page
# print("total windows: {}".format(len(driver.window_handles)))

old_window_id = driver.window_handles[0]
new_window_id = driver.window_handles[1]
driver.switch_to.window(new_window_id)

accept_cookies_btn = driver.find_element(By.ID, "onetrust-accept-btn-handler")
accept_cookies_btn.click()

driver.switch_to.window(old_window_id)

# main page
signin_btn = driver.find_element(By.XPATH, '//*[@id="siteHeader"]/section[2]/nav/div/a[1]')
signin_btn.click()

# account page
name_inp = driver.find_element(By.NAME, 'Login')
name_inp.send_keys("AlexeyGnet")
