import csv
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.hookimpl(hookwrapper=True)
def pytest_exception_interact(node, call, report):
    outcome = yield
    if report.failed:
        browser = getattr(node.cls, 'browser', None)
        if browser:
            screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{node.name}.png")
            browser.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved at: {screenshot_path}")

@pytest.fixture
def browser():
    # Set up the browser
    driver = webdriver.Chrome()
    yield driver
    # Teardown
    driver.quit()


def read_credentials_from_csv():
    # Specify the full file path
    csv_file_path = r'C:\Users\nikhi\OneDrive\Desktop\credentials.csv'

    # Read and print the rows from the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:  # Specify encoding and skip BOM
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

    # Read credentials from CSV file and return a list of tuples
    credentials_list = []
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:  # Specify encoding and skip BOM
        reader = csv.DictReader(file)
        for row in reader:
            # Split the combined key into separate keys for username and password
            username, password = row['username,password'].split(',')
            credentials_list.append((username.strip(), password.strip()))  # Remove leading/trailing whitespaces
    return credentials_list


@pytest.mark.parametrize("username, password", read_credentials_from_csv())
def test_login(browser, username, password):
    # Use the credentials to log in
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    # Add assertions to verify login success or failure
    assert "inventory" in browser.current_url.lower(), "Login failed"
