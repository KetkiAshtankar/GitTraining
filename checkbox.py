from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the URL
url = "https://practice.expandtesting.com/checkboxes"

# Initialize the WebDriver (assumes you have the appropriate driver installed, e.g., chromedriver)
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

# Wait for the checkboxes to be clickable
wait = WebDriverWait(driver, 10)
checkbox1 = wait.until(EC.element_to_be_clickable((By.ID, "checkbox1")))
checkbox2 = wait.until(EC.element_to_be_clickable((By.ID, "checkbox2")))

checkbox1.click()
# Close the browser
# driver.quit()


