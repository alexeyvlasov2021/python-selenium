import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#options needed to keep browser opened after script is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("http://127.0.0.1:5500/index.html")

select_element = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'cars')))
select = Select(select_element)

# get list of options
option_list = select.options

print("+++++++++options text+++++++++")
for option in option_list:
    print(option.text)

select.select_by_value('mercedes')

selected_option_list = select.all_selected_options
print("+++++++++selected options text+++++++++")
for option in selected_option_list:
    print(option.text)
# result: single option is selected - Mercedes

multi_select = wait.until(expected_conditions.element_to_be_clickable((By.NAME, 'multi')))
select2 = Select(multi_select)

multi_selected_option_list = select2.all_selected_options
print("+++++++++multi selected options text (default)+++++++++")
for option in multi_selected_option_list:
    print(option.text)
# result: no option is printed - nothing is selected

select2.select_by_visible_text('Ham')
select2.select_by_visible_text('Sausages')

multi_selected_option_list = select2.all_selected_options
print("+++++++++multi selected options text (after selection)+++++++++")
for option in multi_selected_option_list:
    print(option.text)
# result: multiple options are printed - Ham and Sausages selected



group_select = wait.until(expected_conditions.element_to_be_clickable((By.NAME, 'foods')))
select3 = Select(group_select)
group_option_list = select3.options
print("+++++++++grouped select options+++++++++")
for option in group_option_list:
    print(option.text)
#result: printed list of options without groups

select3.select_by_visible_text("Cod")
print("+++++++++grouped selected options+++++++++")
group_options_selected = select3.all_selected_options
for option in group_options_selected:
    print(option.text)
# result: selected option is printed - Cod
