from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from selenium import webdriver

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.fullscreen_window()
web  = driver.get('https://languid-legs-production.up.railway.app/list')

add_scholar = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/a')
print(add_scholar)
add_scholar.click()
time.sleep(1)

username = driver.find_element(By.ID,'username')
username.send_keys('R@sap.com')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('1234')
submit = driver.find_element(By.XPATH,'/html/body/div[1]/form/button')
submit.click()
time.sleep(1)

driver.find_element(By.ID,'firstName').send_keys('TestFirstName')
driver.find_element(By.ID,'lastName').send_keys('TestLastName')
driver.find_element(By.ID,'email').send_keys('Test4@Email.com')
driver.find_element(By.ID,'currentOrg').send_keys('TestORG')
driver.find_element(By.ID,'orgRole').send_keys('TestRole')
driver.find_element(By.ID,'batch').send_keys('TestBatch')
driver.find_element(By.ID,'degree').send_keys('TestDegree')
driver.find_element(By.ID,'phone').send_keys('TestPhone')
driver.find_element(By.ID,'schoolName').send_keys('TestSchool')
driver.find_element(By.ID,'password').send_keys('TestPassword')
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/form/div[12]/button').click()
time.sleep(12)

# input_element.send_keys('Avishto Banerjee'+Keys.ENTER)
