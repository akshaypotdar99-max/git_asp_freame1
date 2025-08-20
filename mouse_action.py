import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os

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

#time.sleep(5)

action = ActionChains(driver)
Download_icon = driver.find_element(By.XPATH,"(//i[@data-qa-id='gallery_icon_download'])[2]")
action.move_to_element(Download_icon).perform()
#time.sleep(2)

wait.until(lambda _ : driver.find_element(By.XPATH,"(//a[text()='Full Size'])[1]").is_displayed())
action.move_to_element(driver.find_element(By.XPATH,"(//a[text()='Full Size'])[1]")).click().perform()
time.sleep(2)
while True:
    if os.path.exists(r"C:\Users\akshay.potdar\Downloads\Cleanuptest asp 30 4 1 (4) (3).jpg"):
        print("✅Full size File downloaded:")
        break

assert os.path.exists(r"C:\Users\akshay.potdar\Downloads\Cleanuptest asp 30 4 1 (4) (3).jpg")

action.move_to_element(Download_icon).perform()
wait.until(lambda _ : driver.find_element(By.XPATH,"(//a[text()='Reduced Size'])[1]").is_displayed())
action.move_to_element(driver.find_element(By.XPATH,"(//a[text()='Reduced Size'])[1]")).click().perform()
while True:
    if os.path.exists(r"C:\Users\akshay.potdar\Downloads\Cleanuptest asp 30 4 1 (4) (4).jpg"):
        print("✅Lower size File downloaded:")
        break

assert os.path.exists(r"C:\Users\akshay.potdar\Downloads\Cleanuptest asp 30 4 1 (4) (4).jpg")