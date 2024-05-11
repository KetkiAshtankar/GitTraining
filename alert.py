from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (assumes you have the appropriate driver installed, e.g., chromedriver)
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://www.hyrtutorials.com/p/alertsdemo.html")

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@id='alertBox']"))
)
# element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-danger']")))
driver.find_element(By.XPATH,"//button[@id='alertBox']").click()

alert = driver.switch_to.alert
print("Alert text:", alert.text)  # Print the alert text
alert.accept()