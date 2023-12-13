#https://musaifchat.netlify.app/chat
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://musaifchat.netlify.app/chat")

driver.maximize_window()

driver.find_element(By.NAME,"email").send_keys("test@gmail.com")
driver.find_element(By.NAME,"password").send_keys("123456")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(2)
driver.get("https://musaifchat.netlify.app/chat")
time.sleep(5)
users=driver.find_elements(By.CLASS_NAME,"user_wrapper")
for index, value in enumerate(users):
  #print(usr.text)
  value = value.text.lower()
  if value == "md musaif":
    print("Musaif user found",index)
    print(len(value))
    users[index].click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div[2]/form/div[1]/input").send_keys("hello im sending this msg using selenium ")
    driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/form/div[2]/button').click()
    #users.click()
    time.sleep(5)
    break

time.sleep(5)