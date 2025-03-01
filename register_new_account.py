from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

# Setup ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Setup timeout 10 detik
driver.set_page_load_timeout(60)
# Akses URL
driver.get('https://www.cermati.com/app/gabung')
# Wait time for content
time.sleep(5)

# Scenario register
driver.find_element(By.ID,"mobilePhone").send_keys("089637420158")
driver.find_element(By.ID,"email").send_keys("posmaryan@mailinator.com")
driver.find_element(By.ID,"firstName").send_keys("posma")
driver.find_element(By.ID,"lastName").send_keys("ryan")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div/div[2]/div/button").click()
driver.quit()