from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image



class SuperSqa:
    url = "http://demostore.supersqa.com/"

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)
        self.wait = WebDriverWait(self.driver, 5)

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def add_beaine_with_logo(self):
        add_btn = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//a[contains(@aria-label, "Beanie with Logo")]')))
        add_btn.click()

    def add_hoodie_with_zipper(self):
        add_btn = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//a[contains(@aria-label, "Hoodie with Zipper")]')))
        add_btn.click()

    def validate_items_count(self, expected_count):

        # does not work as element text change takes some time
        # count_text = self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "a.cart-contents>span.count"))).text
        # count = int(count_text.split(" ")[0])
        # print(f"your count value is: {count}")
        # print(type(count))
        # assert count == 2, "wrong checkout items count detected"


        # wait for element text match
        try:
            # works with exact text match
            # self.wait.until(
            # expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "a.cart-contents>span.count"),f"{expected_count} items"))

            #work when substring match - expected count is present in element text
            self.wait.until(
                expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "a.cart-contents>span.count"),
                                                                  f"{expected_count}"))
        except TimeoutException:
            # executed in case of invalid items count or message text

            # checks text
            count_text = self.driver.find_element(By.CSS_SELECTOR, "a.cart-contents>span.count").text

            # prints error
            print(f"unexpected checkout items count detected: {count_text}")

            # element present on the page to scroll in case of error
            search_fld = self.driver.find_element(By.CSS_SELECTOR, "input#woocommerce-product-search-field-0")

            # scrolling action
            ActionChains(driver=self.driver)\
                .scroll_to_element(search_fld)\
                .perform()

            # https://www.browserstack.com/guide/take-screenshot-with-selenium-python
            # making screenshot
            self.driver.save_screenshot("./screens/items_count.png")

            # opening screenshot
            my_screen = Image.open("./screens/items_count.png")
            my_screen.show()

    def open_cart(self):
        menu_item = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "ul.nav-menu li.page-item-7 a")))
        menu_item.click()

    def enter_coupon_code(self, code):
        text_input = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input#coupon_code")))
        text_input.send_keys(code)

        enter_btn = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[name='apply_coupon']")))
        enter_btn.click()

    def validate_coupon_success_message(self):
        try:
            self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "div.woocommerce-message"), "Coupon code applied successfully"))
            element = self.driver.find_element(By.CSS_SELECTOR, "div.woocommerce-message")
            element_color = element.value_of_css_property("background-color")

            assert element_color == 'rgba(15, 131, 77, 1)', f"coupon apply message unexpected background color: {element_color}"

        except TimeoutException:
            print("unexpected message after applying coupon")

    def validate_total_price(self, expected_price):
        my_locator ="td[data-title='Total'] span.woocommerce-Price-amount.amount bdi"
        try:
            # format expected price to format 0.00
            # https://realpython.com/how-to-python-f-string-format-float/
            self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, my_locator)
                , f"${expected_price:.2f}"))
        except TimeoutException:
            price = self.driver.find_element(By.CSS_SELECTOR, my_locator).text
            print(f"unexpected total price: {price}")


if __name__ == '__main__':
    site = SuperSqa()
    site.open()
    site.add_beaine_with_logo()
    site.add_hoodie_with_zipper()
    site.validate_items_count(expected_count= 2)
    site.open_cart()
    site.enter_coupon_code("SSQA100")
    site.validate_coupon_success_message()
    site.validate_total_price(expected_price= 0)
    site.driver.quit()
