import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# guide
# https://www.youtube.com/watch?v=xNqWMXgSsQ4

from selenium import webdriver
import csv

# here the csv file is hosted in the same package as python file
# csv_file = 'csv_demo.csv'
csv_file = '/Users/alexeyvlasov/Documents/Automation/Selemium-Python/Selenium/my_scripts/data_driven/tables/csv_demo.csv'
# this file is used to output data from csv
test_data = []

# open the file in readonly mode 'r'
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    # looping through the csv file and append data to the list
    for row in reader:
        test_data.append(row)

# output is a list of dictionaries - pairs of keys:values
print(test_data)
# select item of index 3 from list, get value with keys
print(test_data[3].get('username'))
print(test_data[3].get('password'))


def run_test(data):
    # chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(chrome_options)
    # driver.get("http://demostore.supersqa.com/my-account/")
    # driver.implicitly_wait(10)
    # driver.maximize_window()
    #
    # username_fld = driver.find_element(By.ID, 'username')
    # password_fld = driver.find_element(By.ID, 'password')
    #
    # # update password field attribute with js script to make its value visible
    # driver.execute_script('arguments[0].setAttribute("type", "text")', password_fld)

    for row in data:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.get("http://demostore.supersqa.com/my-account/")
        driver.implicitly_wait(10)
        driver.maximize_window()

        username_fld = driver.find_element(By.ID, 'username')
        password_fld = driver.find_element(By.ID, 'password')

        # update password field attribute with js script to make its value visible
        driver.execute_script('arguments[0].setAttribute("type", "text")', password_fld)

        u = row.get('username')
        p = row.get('password')
        username_fld.send_keys(u)
        password_fld.send_keys(p)
        time.sleep(2)
        username_fld.clear()
        password_fld.clear()
        time.sleep(3)
        driver.quit()

    # time.sleep(3)
    # driver.quit()

run_test(test_data)
