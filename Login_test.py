import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://basetenant.stg.adzu.io/#page/Assets")
driver.maximize_window()
driver.implicitly_wait(8)

driver.find_element(By.ID,"us1").send_keys("akshaypotdar99@gmail.com")
driver.find_element(By.ID,"pa1").send_keys("Bharat@123")
driver.find_element(By.CSS_SELECTOR,".btn.btn-primary.login").click()
time.sleep(7)
assert driver.find_element(By.CSS_SELECTOR,"div.checkbox").is_displayed()
time.sleep(2)
ele1 = driver.find_element(By.CLASS_NAME,"gallery-item-action-menu-box")
action=ActionChains(driver)
action.move_to_element(ele1).perform()
scroll_origin = ScrollOrigin.from_element(ele1)
action.scroll_from_origin(scroll_origin, 0, 200).perform()
time.sleep(5)
driver.quit()