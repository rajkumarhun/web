from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Path to your WebDriver executable
driver_path = 'path/to/your/webdriver'


# Open Facebook
driver.get('https://www.facebook.com')

# Log in
username = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'pass')

# Enter your Facebook login credentials here
username.send_keys('your_facebook_email')
password.send_keys('your_facebook_password')
password.send_keys(Keys.RETURN)

time.sleep(5)  # Wait for login to complete

# Open Messenger
driver.get('https://www.facebook.com/messages')

time.sleep(5)  # Wait for Messenger to load

# Find the new message button
new_message_button = driver.find_element(By.XPATH, '//a[@aria-label="New Message"]')
new_message_button.click()

time.sleep(2)  # Wait for new message modal to open

# Enter recipient's name
recipient = driver.find_element(By.XPATH, '//input[@aria-label="To:"]')
recipient.send_keys('recipient_name')
time.sleep(2)  # Wait for recipient to be selectable
recipient.send_keys(Keys.RETURN)

# Enter the message
message_box = driver.find_element(By.XPATH, '//div[@aria-label="Type a message..."]')
message_box.click()
ActionChains(driver).send_keys('Hello, this is a test message!').perform()

# Send the message
ActionChains(driver).send_keys(Keys.RETURN).perform()

time.sleep(2)  # Wait for message to send

# Close the browser
driver.quit()
