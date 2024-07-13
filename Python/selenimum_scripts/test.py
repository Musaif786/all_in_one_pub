from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
Testing file
'''

# Open the browser
driver = webdriver.Edge()

# Set the implicitly wait timeout to 10 seconds
driver.implicitly_wait(10)
driver.maximize_window()

# Open the website
driver.get("https://musaifchat.netlify.app/login")

# Try to click on the element with the ID 'someid'
try:
  print(driver.title)
  driver.find_element(By.NAME, 'email').send_keys('test@gmail.com')
  driver.find_element(By.NAME, 'password').send_keys('123456')

  #login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
  login_button = driver.find_element(By.XPATH, '//*[@id="root"]/section/form/div[3]/button')
  login_button.click()
  users = driver.find_elements(By.XPATH,"//div[@class='user_wrapper selected_user']//div")
  for i in users:
    print(i.text)
    
  time.sleep(12)
  driver.find_element(By.XPATH,'//*[@id="root"]/nav/div/button/i').click()
  #driver.find_element(By.CSS_SELECTOR,'')
  #driver.close()

except Exception:
  print("Element not found or not clickable")

time.sleep(2)

