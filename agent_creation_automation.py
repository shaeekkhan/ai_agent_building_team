import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

dotenv_path = os.path.join('.venv', '.env')

# Load the .env file explicitly
load_dotenv(dotenv_path)

# Get environment variables
URL = os.getenv('URL')
ID = os.getenv('ID')
PASSWORD = os.getenv('PASSWORD')

# Setup webdriver
driver = webdriver.Chrome()  # Make sure you have chromedriver in your PATH
driver.maximize_window()
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for elements

try:
    # 1. Navigate to the website
    driver.get(URL)

    # 2. Fill in login details
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'email')))  # Adjust selector as needed
    password_field = wait.until(EC.presence_of_element_located((By.ID, 'password')))  # Adjust selector as needed

    username_field.send_keys(ID)
    password_field.send_keys(PASSWORD)

    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/div/div/form/div[4]/button')))  # Adjust selector as needed
    login_button.click()

    # 3. Wait for the site to load
    time.sleep(5)  # You might want to replace this with a more robust wait condition

    # 4. Click on the profile CTA
    profile_cta = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/aside/div/div[4]/div')))  # Adjust selector as needed
    profile_cta.click()

    # 5. Wait for modal to open
    time.sleep(2)  # Again, consider replacing with a more robust wait condition

    # 6. Find and click on "My Agent"
    my_agent_link = wait.until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/ul/li/span/div/a[3]/div')))  # Adjust selector as needed
    my_agent_link.click()

    # Wait for page to load
    time.sleep(3)  # Consider replacing with a more robust wait condition

    # 7. Click on "+ Create Agent" button
    create_agent_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/main/div[2]/section/div[2]/div/div/aside/div/div[1]/button')))  # Adjust selector as needed
    create_agent_button.click()

    # 8. Wait for agent creation modal to open
    time.sleep(2)  # Consider replacing with a more robust wait condition


except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()
