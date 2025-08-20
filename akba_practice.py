from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://duckduckgo.com")
driver.maximize_window()

driver.find_element(By.ID, "searchbox_input").send_keys("Python programming")

driver.find_element(By.CLASS_NAME, "searchbox_iconWrapper__qAk7y").click()

driver.save_screenshot("before_cross.png")

time.sleep(2)

actions = ActionChains(driver)  # Python

#hoverable = driver.find_element(By.CSS_SELECTOR,"button[aria-label='clear'] svg")  # //button[@aria-label='clear']//*[name()='svg']")
# Locate element
element = driver.find_element(By.CSS_SELECTOR,"button[aria-label='search']")  # Google's search box
# Get element size
size = element.size
width = size['width']
height = size['height']
print(width)

# move to element with offset: (-width/2 + 1, 0) → near left edge
actions.move_to_element_with_offset(element, -width/2 -15, 0).pause(2).click().perform()

time.sleep(2)

driver.find_element(By.CLASS_NAME, "KzVoRLlICt8isnbHKZpL").send_keys("Python programming by SDET")

driver.find_element(By.CLASS_NAME, "_212PfUnoxOJ9_9eYg13j").click()  # Correct Line

# driver.find_element(By.CLASS_NAME,"_212PfUnoxOJ9_9eYg13j").click()


print("Page Title:", driver.title)

print("Current URL:", driver.current_url)

driver.save_screenshot("Python_ProgrmmingScreenshot.png")

time.sleep(4)

driver.quit()

