import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
wait.until(lambda _ : driver.find_element(By.CSS_SELECTOR,"div.checkbox").is_displayed())

assert driver.find_element(By.CSS_SELECTOR,"div.checkbox").is_displayed()

time.sleep(5)

driver.find_element(By.XPATH,"(//div[@class='filter-content inject-widget-container']//div)[22]").click()
time.sleep(2)
options = driver.find_elements(By.CSS_SELECTOR,"div[class^='v-menu__content']>div>div>div>div")
for option in options:
    if option.text == "Approved":
        option.click()
        break

time.sleep(2)
Apply_button = driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-primary']")
wait.until(lambda _ : Apply_button.is_enabled())
Apply_button.click()
wait.until(lambda _ : driver.find_element(By.CSS_SELECTOR,"div.checkbox").is_displayed())

approval_status= driver.find_element(By.XPATH,"(//div[@class='filter-content inject-widget-container']//div)[22]").text
assert approval_status=="Approved"
print(approval_status)

time.sleep(3)
asset_names = driver.find_elements(By.CSS_SELECTOR,"div[class=name]")
asset_name_text_actual = []
asset_name_text_expected = ["cleanuptest_asp_791985","cleanuptest_asp_179595"]
for asset in asset_names:
    asset_name_text_actual.append(asset.text)

assert asset_name_text_actual == asset_name_text_expected
print(asset_name_text_actual)



