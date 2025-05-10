import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

pytestmark = [pytest.mark.frontend, pytest.mark.frontend2]

@pytest.mark.some_mark
def test_open_site():
    # options needed to keep browser opened after script is executed
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get("http://demostore.supersqa.com")
    time.sleep(2)
    driver.quit()

@pytest.mark.some_mark
@pytest.mark.regression
def test_print_my_name():
    print("Alexey Vlasov")