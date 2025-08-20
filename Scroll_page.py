import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

#Headless browsers
chrome_options = Options()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(15)

driver.execute_script("window.scrollBy(0,300);")
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(3)
driver.get_screenshot_as_file(r"C:\Users\akshay.potdar\Downloads\screen.png")
time.sleep(3)