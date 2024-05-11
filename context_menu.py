from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://practice.expandtesting.com/context-menu")

# Locate the element that triggers the context menu
context_menu_element = driver.find_element(By.ID, "hot-spot")

# Right-click on the element to open the context menu

ActionChains(driver).context_click(context_menu_element).perform()
alert = driver.switch_to.alert
print("Alert text:", alert.text)  # Print the alert text
alert.accept()