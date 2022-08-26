# Runs for this number of seconds :
seconds = 5

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime

chrome_driver_path = "../resources/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

starttime = datetime.now()
diff = starttime - starttime
while diff.total_seconds() < seconds:
    cookie.click()
    diff = datetime.now() - starttime

