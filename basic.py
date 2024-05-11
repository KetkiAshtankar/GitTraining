from selenium import webdriver


# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.get('https://mylocation.org/')
# # Navigate to the login page
# driver.get("https://www.saucedemo.com")

# # Simple Usage: Finding and interacting with DOM elements
# username_input = driver.find_element_by_xpath("//*[@id='user-name']")
# password_input = driver.find_element_by_xpath("//*[@id='password']")
# login_button = driver.find_element_by_xpath("//input[@type='submit']")


# # Input data into the username and password fields
# username_input.send_keys("standard_user")
# password_input.send_keys("secret_sauce")

# # Click the login button
# login_button.click()

# # Wait for the inventory page to load
# time.sleep(2)

# # Example Explained: Printing the title of the page
# print("Page Title:", driver.title)



# # Walkthrough of the example: Printing the URL of the page
# print("Current URL:", driver.current_url)

# Close the browser
# driver.quit()
