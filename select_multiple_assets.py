import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
import openpyxl

driver = webdriver.Chrome()
driver.get("https://basetenant.stg.adzu.io/#page/TEST-LICENSE-ASSETS")
driver.maximize_window()
driver.implicitly_wait(15)

driver.find_element(By.ID,"us1").send_keys("akshaypotdar99@gmail.com")
driver.find_element(By.ID,"pa1").send_keys("Bharat@123")
driver.find_element(By.CSS_SELECTOR,".btn.btn-primary.login").click()
#time.sleep(7)
#Applying explicit wait
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"div.checkbox")))

assert driver.find_element(By.CSS_SELECTOR,"div.checkbox").is_displayed()
# Get all asset containers
asset_names = ["cleanuptest_asp_746718","cleanuptest_asp_746718","test_asp_Asset_3","test_asp_Asset_4"]
assets = driver.find_elements(By.XPATH, "//div[@class='col-sm-3 gallery-item-container']")

time.sleep(5)

for asset in assets:
    # ✅ Use relative XPath (with dot `.`) to search within each `asset`
    asset_name = asset.find_element(By.XPATH, ".//div/div[4]/div/span").text

    if asset_name in asset_names:
        # ✅ Also use relative XPath for the checkbox
        checkbox = asset.find_element(By.XPATH, ".//div[@class='checkbox']")
        checkbox.click()

driver.quit()
