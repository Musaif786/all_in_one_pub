from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import popup

# url = 'https://opensource-demo.orangehrmlive.com'
# url ="https://www.orangehrm.com/"
# url = "https://demo.nopcommerce.com/software"
url = "https://demo.nopcommerce.com/"

# Open the browser
driver = webdriver.Edge()

# Set the implicitly wait timeout to 10 seconds
driver.implicitly_wait(10)
driver.maximize_window()

# Open the website
driver.get(url)


# by id and name
# driver.find_element(By.ID,"small-searchterms").send_keys("laptop")
# driver.find_element(By.NAME,"q").send_keys("laptop")

#links both partial and link text work as same
# driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

# box = driver.find_elements(By.CLASS_NAME,"item-box")
# print(len(box))
# popup.popupFun(len(box))



# element_xpath = "//a[@href='/electronics']"
# element = driver.find_element(By.XPATH,element_xpath)

# # Get the text content of the element
# element_text = element.text

# # Print the text content
# print("Text content of the element:", element_text)


#full path
# element_path = "/html[1]/body[1]/div[6]/div[3]/div[1]/div[3]/div[1]/div[1]/h1[1]"
#absolute path
# element_path = "/html/body/div[6]/div[3]/div/div[3]/div/div[1]/h1"
# element = driver.find_element(By.XPATH,element_path)
# print(element.text)




time.sleep(5)
driver.close()