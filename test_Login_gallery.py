import math
import time
from math import *

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://basetenant.stg.adzu.io/#page/TEST-LICENSE-ASSETS")
    driver.maximize_window()
    driver.implicitly_wait(15)

    driver.find_element(By.ID, "us1").send_keys("akshaypotdar99@gmail.com")
    driver.find_element(By.ID, "pa1").send_keys("Bharat@123")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.login").click()
    # time.sleep(7)
    # Applying explicit wait
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.checkbox")))

    assert driver.find_element(By.CSS_SELECTOR, "div.checkbox").is_displayed()
    x=16