from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.binary_location = "/Applications/Opera.app/Contents/MacOS/Opera"
ser = Service(ChromeDriverManager().install())
# Автоматически скачивает ChromeDriver подходящей версии
driver = webdriver.Chrome(
    options,
    ser
)

# driver = webdriver.Chrome(
#     service=ser,
#     options=options
# )

driver.get("https://itc.ua/ua/")


# does not work
# selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 135
# Current browser version is 133.0.6943.143 with binary path /Applications/Opera.app/Contents/MacOS/Opera