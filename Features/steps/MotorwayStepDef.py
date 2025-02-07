import time

from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from GeneralFunction.GeneralFunctions import extract_reg_numbers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
results = []

@given('the user logs onto motorway website and enter the car registration number from file')
def step_impl(context):
    # Get the registration details
    global results
    results = extract_reg_numbers()
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')  # Optional: starts Chrome maximized

    # Set up the Chrome service
    service = Service("Drivers/chromedriver.exe")

    # Initialize the driver
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to the website
    context.driver.get("https://motorway.co.uk/")

    act_title = context.driver.title
    expected_title = "Sell My Car | Get Your Highest Offer | Easy & 100% Free"

    if act_title == expected_title:
        context.driver.find_element(By.XPATH, '//*[@id="vrm-input"]').send_keys(results[0])
        context.driver.find_element(By.CSS_SELECTOR,'.Button-module__button-If4h:nth-child(2) > .Button-module__label-SKEy').click()
        time.sleep(20)
        context.driver.find_element(By.XPATH, '//*[@id="mileage-input').send_keys("90000")
        context.driver.find_element(By.XPATH, '//*[@id="mileage-input').send_keys(Keys.RETURN)
        time.sleep(20)








