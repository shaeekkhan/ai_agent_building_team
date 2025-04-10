import os
import sys
import time
from dotenv import load_dotenv
from session_manager import load_agents_from_file
from playwright.sync_api import sync_playwright

dotenv_path = os.path.join('.venv', '.env')
load_dotenv(dotenv_path)

URL = os.getenv('URL')
ID = os.getenv('ID')
PASSWORD = os.getenv('PASSWORD')

if len(sys.argv) < 2:
    print("No session file provided. Exiting.")
    sys.exit()

session_file = sys.argv[1]


# Start Playwright Automation
def upload_agents():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch the browser
        page = browser.new_page(viewport={"width": 1920, "height": 1080})  # Set to Full HD resolution
        page.goto(URL)

        # Step 1: Login
        page.locator("#email").fill(ID)
        page.locator("#password").fill(PASSWORD)
        page.locator("xpath=//*[@id='root']/div[1]/div/div/div/form/div[4]/button").click()
        page.wait_for_timeout(5000)

        # Step 2: Navigate to 'My Agent' section
        page.locator("xpath=//*[@id='root']/main/aside/div/div[4]/div").click()
        page.wait_for_timeout(3000)
        page.locator("xpath=/html/body/div[2]/div/ul/li/span/div/a[3]").click()
        page.wait_for_timeout(3000)

        # Load agents from session
        agents = load_agents_from_file(session_file)

        for i, agent in enumerate(agents):
            print(f"Uploading agent {i+1}: {agent['name']}")

            # Step 3: Click "+ Create Agent" before each iteration
            page.locator("xpath=//*[@id='root']/main/div[2]/section/div[2]/div/div/aside/div/div[1]/button").click()
            page.wait_for_timeout(2000)

            # Step 4: Fill Agent Details
            page.locator('xpath=//*[@id="name"]').fill(agent["name"])
            page.wait_for_timeout(2000)
            page.locator('xpath=//*[@id="instructions"]').fill(agent["instructions"])
            page.wait_for_timeout(2000)
            page.locator('xpath=//*[@id="description"]').fill(agent["description"])
            page.wait_for_timeout(2000)

            # Step 5: Click 'Generate Image' Radio Button
            page.locator("xpath=//*[@id='photoOption']/label[1]/span[1]").click()
            page.wait_for_timeout(2000)

            # Step 6: Select Category
            page.locator("xpath=//*[@id='rc-tabs-1-panel-unoptimized-data']/form/div[5]/div/div[2]/div/div/div/div").click()
            page.wait_for_timeout(2000)
            page.locator("xpath=/html/body/div[4]/div/div/div[2]/div[1]/div/div/div[8]/div").click()
            page.wait_for_timeout(2000)

            # Step 7: Select AI Model
            page.locator("xpath=//*[@id='rc-tabs-1-panel-unoptimized-data']/form/div[7]/div/div[2]/div/div/div/div").click()
            page.wait_for_timeout(2000)
            page.locator("xpath=/html/body/div[5]/div/div/div[2]/div/div/div/div[5]/div").click()
            page.wait_for_timeout(2000)

            # Step 8: Click 'Create Agent' Button
            page.locator("xpath=//*[@id='rc-tabs-1-panel-unoptimized-data']/form/div[14]/div/div/div/div/button/span").click()
            page.wait_for_timeout(5000)  # Adjust based on site response time

        print("All agents have been created. ✅")
        browser.close()


# Run the function
upload_agents()
