from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

'''
WORKING CODE

'''

# Open the browser
driver = webdriver.Edge()

# Set the implicitly wait timeout to 10 seconds
driver.implicitly_wait(30)

# Open the website
driver.get("https://musaifchat.netlify.app/login")
driver.maximize_window()

# Try to click on the element with the ID 'someid'
try:
  driver.find_element(By.NAME, 'email').send_keys('test@gmail.com')
  driver.find_element(By.NAME, 'password').send_keys('123456')

#   login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
#   login_button.click()
  login_button = driver.find_element(By.XPATH, '//*[@id="root"]/section/form/div[3]/button')
  login_button.click()
  time.sleep(4)
  driver.find_element(By.XPATH,'//*[@id="root"]/nav/div/button/i').click()
  #driver.close()

except Exception:
  print("Element not found or not clickable")

time.sleep(5)