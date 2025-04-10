import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from session_manager import load_agents_from_file

dotenv_path = os.path.join('.venv', '.env')
load_dotenv(dotenv_path)

URL = os.getenv('URL')
ID = os.getenv('ID')
PASSWORD = os.getenv('PASSWORD')

if len(sys.argv) < 2:
    print("No session file provided. Exiting.")
    sys.exit()

session_file = sys.argv[1]

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    driver.get(URL)
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'email')))
    password_field = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    username_field.send_keys(ID)
    password_field.send_keys(PASSWORD)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/div/div/form/div[4]/button')))
    login_button.click()
    time.sleep(5)

    profile_cta = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/aside/div/div[4]/div')))
    profile_cta.click()
    my_agent_link = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/ul/li/span/div/a[3]/div')))
    my_agent_link.click()
    time.sleep(3)

    create_agent_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/div[2]/section/div[2]/div/div/aside/div/div[1]/button')))
    create_agent_button.click()
    time.sleep(2)

    agents = load_agents_from_file(session_file)

    for agent in agents:
        print(f"Uploading agent: {agent['name']}")

        name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rc-tabs-1-panel-unoptimized-data"]/form/div[1]/div/div[2]/div')))
        instructions_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rc-tabs-1-panel-unoptimized-data"]/form/div[3]/div/div[2]/div')))
        description_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rc-tabs-1-panel-unoptimized-data"]/form/div[4]/div/div[2]/div')))

        name_field.send_keys(agent["name"])
        instructions_field.send_keys(agent["instructions"])
        description_field.send_keys(agent["description"])

        generate_image_radio = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="photoOption"]/label[1]/span[1]')))
        generate_image_radio.click()

        category_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-tabs-1-panel-unoptimized-data"]/form/div[5]/div/div[2]/div/div/div/div')))
        category_dropdown.click()
        category_option = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[2]/div[1]/div/div/div[8]/div')))
        category_option.click()

        ai_model_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-tabs-1-panel-unoptimized-data"]/form/div[7]/div/div[2]/div/div/div/div')))
        ai_model_dropdown.click()
        ai_model_option = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div/div/div[5]/div')))
        ai_model_option.click()

        create_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-tabs-1-panel-unoptimized-data"]/form/div[14]/div/div/div/div/button/span')))
        create_button.click()

        WebDriverWait(driver, 5).until(EC.staleness_of(create_button))

    print("Creation is done.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    driver.quit()
