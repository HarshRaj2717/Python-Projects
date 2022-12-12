from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "resources/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page") # Open a site
articlescount = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# print(articlescount.text)
articlescount.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("python", Keys.ENTER)

# Close a tab
# driver.close()
# Close the browser
# driver.quit()
