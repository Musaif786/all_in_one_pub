from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''
Testing file
'''

# Open the browser
driver = webdriver.Edge()

# Set the implicitly wait timeout to 10 seconds
driver.implicitly_wait(60)
driver.maximize_window()

# Open the website
driver.get("https://solugenix.criterionhcm.com/ui/#dashboard")

# Try to click on the element with the ID 'someid'
try:
  print(driver.title)
  
#   driver.find_element(By.NAME, 'email').send_keys('test@gmail.com')
#   driver.find_element(By.NAME, 'password').send_keys('123456')

  #login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
  login_button = driver.find_element(By.XPATH, '//*[@id="login_wrapper"]/input').send_keys('musaif.mohammed@solugenix.com')
  #//*[@id="login_submit"]
  login_button_click = driver.find_element(By.XPATH, '//*[@id="login_submit"]')
  login_button_click.click()

  login_button_click_auth = driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys('musaif')
  
  driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
  
  time.sleep(3)
  #ogin_button_click_auth.click()
  paswrd = driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys('password')
  time.sleep(3)
  
  success_indicator = WebDriverWait(driver, 300).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="criterion_view_ess_navigation_dynamic_button-1340-btnIconEl"]'))  # Replace with actual identifier
  )

  driver.find_element(By.XPATH, '//*[@id="criterion_view_ess_navigation_dynamic_button-1340-btnIconEl"]').click()
  time.sleep(3)
#   timesheet =  driver.find_element(By.XPATH, '//*[@id="criterion_view_ess_navigation_dynamic_button-*"]')
#   timesheet.click()

#   timesheet1 =  driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/a[3]/span[1]/span[1]/span[1]')
#   timesheet1.click()
  #/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/a[3]/span[1]/span[1]/span[1]

#   users = driver.find_elements(By.XPATH,"//div[@class='user_wrapper selected_user']//div")
#   for i in users:
#     print(i.text)
    
#   time.sleep(12)
#   driver.find_element(By.XPATH,'//*[@id="root"]/nav/div/button/i').click()
  #driver.find_element(By.CSS_SELECTOR,'')
  #driver.close()

except Exception:
  print("Element not found or not clickable")

time.sleep(120)

