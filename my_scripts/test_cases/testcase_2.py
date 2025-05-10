import os
import time
import math

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class EverveSite:
    url = "https://everve.cc/"

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(self.chrome_options)
        self.wait = WebDriverWait(driver=self.driver, timeout=5)

    def open_site(self):
        self.driver.get(url=self.url)
        self.driver.maximize_window()

    def skip_cookies(self):
        try:
            accept_cookies_btn = self.wait.until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//button[text() = 'Alle akzeptieren']")))
            accept_cookies_btn.click()
        except TimeoutException:
            pass

    def select_mans_section(self):
        mans_btn = self.wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "li#mega-menu-item-234514>a")))
        mans_btn.click()

    def click_ezero(self):
        ezero_btn = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, "li#mega-menu-item-everve-subnavi-image-20>a")))
        ezero_btn.click()

    def click_first_product(self):
        first_product = self.wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a.woocommerce-LoopProduct-link")))
        first_product.click()

    def choose_seat(self):
        crazy_btn = self.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Wähle deinen')]")))
        crazy_btn.click()

    def click_configure(self):
        configure_btn = self.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='konfigurieren']")))
        configure_btn.click()

    def select_bike_type(self):
        rennrad_btn = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "label[for='rennrad']")))
        rennrad_btn.click()

    def bike_type_submit(self):
        submit_btn = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a#radtyp-submit")))
        submit_btn.click()

    def set_weight(self):
        range_input = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input#weight")))

        # shifting range with right arrow button
        # initial position of cursor is 50 at left side

        target_value = 105
        min_value =  int(range_input.get_attribute("min") or 0)

        # running loop and clicking arrow right button. starting point is 51
        # end point is target_value
        for i in range(min_value+1, target_value+1):
            range_input.send_keys(Keys.ARROW_RIGHT)



        # wrong approach
        # set value with js
        # self.driver.execute_script("arguments[0].value = arguments[1];", range_input, 88)


        # chat gpt recommended - calls necessary events - site updates data
        # self.driver.execute_script("""
        #     arguments[0].value = arguments[1];
        #     arguments[0].dispatchEvent(new Event('input'));
        #     arguments[0].dispatchEvent(new Event('change'));
        # """, range_input, 88)


        # working, but not ideal accuracy
        # set value by clicking input range
        # target_value = 78
        # mid_value = 85
        # width = int(range_input.size["width"])
        # min_val =  int(range_input.get_attribute("min") or 0)
        # max_val =  int(range_input.get_attribute("max") or 100)
        #
        # fraction = int(width/(max_val - min_val))
        # target_offset = (target_value - mid_value) * fraction
        #
        # ActionChains(self.driver)\
        #     .move_to_element_with_offset(range_input, target_offset, 0) \
        #     .click()\
        #     .perform()

    def weight_submit(self):
        submit_btn = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a#gewicht-submit")))
        submit_btn.click()

if __name__ == '__main__':
    es = EverveSite()
    es.open_site()
    es.skip_cookies()
    es.select_mans_section()
    es.click_ezero()
    es.click_first_product()
    es.choose_seat()
    es.click_configure()
    es.select_bike_type()
    es.bike_type_submit()
    es.set_weight()
    es.weight_submit()
