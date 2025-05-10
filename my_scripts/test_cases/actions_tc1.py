import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def register_new_user(email, password):
    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(chrome_options)

    driver.get('http://demostore.supersqa.com/')
    driver.maximize_window()
    wait = WebDriverWait(driver, timeout=5)

    # home page
    my_account = wait.until(
        expected_conditions.element_to_be_clickable((By.XPATH, '//ul[@class="nav-menu"]/li/a[text() = "My account"]')))
    my_account.click()

    # account page
    h1_title = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'h1.entry-title')))
    assert h1_title.text == 'My account', 'wrong account page title'

    account_page_url = driver.current_url
    assert account_page_url == 'http://demostore.supersqa.com/my-account/', 'unexpected url for account page'

    email_input = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'reg_email')))
    password_input = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'reg_password')))
    register_btn = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'button[value="Register"]')))

    email_input.send_keys(email)
    password_input.send_keys(password)
    register_btn.click()

    # account page after user is registered
    nav_elements = wait.until(expected_conditions.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "nav.woocommerce-MyAccount-navigation ul li")))
    greeting_text = wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//div[@class='woocommerce-MyAccount-content']/p[1]")))
    logout_btn = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//li/a[text() ='Logout']")))

    assert len(nav_elements) == 6, "wrong number of nav elements"
    assert "Hello" in greeting_text.text, "wrong greeting text"

    logout_btn.click()

    # account log off
    second_header = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//h2)[2]")))

    assert second_header.text == "Register", "wrong header text after logoff"

    time.sleep(2)
    driver.quit()

def register_existed_user(email, password):
    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(chrome_options)

    driver.get('http://demostore.supersqa.com/')
    driver.maximize_window()
    wait = WebDriverWait(driver, timeout=5)

    # home page
    my_account = wait.until(
        expected_conditions.element_to_be_clickable((By.XPATH, '//ul[@class="nav-menu"]/li/a[text() = "My account"]')))
    my_account.click()

    # account page
    h1_title = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'h1.entry-title')))
    assert h1_title.text == 'My account', 'wrong account page title'

    account_page_url = driver.current_url
    assert account_page_url == 'http://demostore.supersqa.com/my-account/', 'unexpected url for account page'

    email_input = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'reg_email')))
    password_input = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'reg_password')))
    register_btn = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'button[value="Register"]')))

    email_input.send_keys(email)
    password_input.send_keys(password)
    register_btn.click()

    error_msg = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, '//*[@id="content"]/div/div[1]/ul/li/strong')))
    page_code = driver.page_source
    assert 'An account is already registered' in page_code, "wrong error when registered existed user"

    time.sleep(2)
    driver.quit()


def login(email, password):
    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(chrome_options)

    driver.get('http://demostore.supersqa.com/')
    driver.maximize_window()
    wait = WebDriverWait(driver, timeout=5)

    # home page
    my_account = wait.until(
        expected_conditions.element_to_be_clickable((By.XPATH, '//ul[@class="nav-menu"]/li/a[text() = "My account"]')))
    my_account.click()

    # account page
    h1_title = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'h1.entry-title')))
    assert h1_title.text == 'My account', 'wrong account page title'

    account_page_url = driver.current_url
    assert account_page_url == 'http://demostore.supersqa.com/my-account/', 'unexpected url for account page'

    username_input = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'username')))
    password_input = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'password')))
    login_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'button[name="login"]')))

    username_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()

    # account page after user is logged in
    nav_elements = wait.until(expected_conditions.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "nav.woocommerce-MyAccount-navigation ul li")))
    greeting_text = wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//div[@class='woocommerce-MyAccount-content']/p[1]")))
    logout_btn = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//li/a[text() ='Logout']")))

    assert len(nav_elements) == 6, "wrong number of nav elements"
    assert "Hello" in greeting_text.text, "wrong greeting text"

    logout_btn.click()

    # account log off
    second_header = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//h2)[2]")))

    assert second_header.text == "Register", "wrong header text after logoff"

    time.sleep(2)
    driver.quit()
