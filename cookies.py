from selenium import webdriver
from selenium.webdriver.common.by import By
# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open SauceDemo website
driver.get("https://www.saucedemo.com/")

# Display cookies before login
print("Cookies before login:")
for cookie in driver.get_cookies():
    print(cookie)

# Perform login (assuming username and password fields have IDs "user-name" and "password")    
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Display cookies after login
print("\nCookies after login:")
for cookie in driver.get_cookies():
    print(cookie)

# Close the browser
driver.quit()
