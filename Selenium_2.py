from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)


driver_path = "My_path/chromedriver.exe"


service = Service(executable_path=driver_path)  
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.eghtesadnews.com/")
page_source = driver.page_source
print(page_source)

driver.quit()
