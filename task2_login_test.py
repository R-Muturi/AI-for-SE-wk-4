# Task 2: Automate login page testing using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run browser in headless mode
driver = webdriver.Chrome(options=chrome_options)

# Open login page
driver.get("https://example.com/login")  # Replace with actual URL

# Test case: Valid login
driver.find_element(By.ID, "username").send_keys("valid_user")
driver.find_element(By.ID, "password").send_keys("valid_pass")
driver.find_element(By.ID, "login").click()
time.sleep(2)  # Wait for page to load

success = driver.find_element(By.ID, "welcome").is_displayed()  # Check for success message
print("Valid login success:", success)

# Test case: Invalid login
driver.get("https://example.com/login")
driver.find_element(By.ID, "username").send_keys("invalid_user")
driver.find_element(By.ID, "password").send_keys("wrong_pass")
driver.find_element(By.ID, "login").click()
time.sleep(2)

error_displayed = driver.find_element(By.ID, "error").is_displayed()  # Check error message
print("Invalid login error displayed:", error_displayed)

# Close browser
driver.quit()
