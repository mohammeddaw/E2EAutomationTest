import time

from selenium import webdriver
from GeneralFunction.GeneralFunctions import extract_reg_numbers
from Pages.Base_Page import BasePage
from Pages.EnterMileagePage import EnterMileagePage
from Pages.MotorWayHomePage import HomePageForMotorWay
from behave import *


class MotorwayTest(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @given('the user logs onto motorway website and enter the car registration number from file')
    def step_impl(context):
        context.driver =  webdriver.Chrome()

        # Get the registration details
        global results
        results = extract_reg_numbers()
        homepage = HomePageForMotorWay(context.driver)
        mileagepage = EnterMileagePage(context.driver)

        # Navigate to the website
        homepage.open_page("https://motorway.co.uk/")

        act_title = context.driver.title
        expected_title = "Sell My Car | Get Your Highest Offer | Easy & 100% Free"

        if act_title == expected_title:
            time.sleep(10)
            homepage.enter_car_reg(results[0])
            homepage.value_your_car()
            mileagepage.enter_car_mileage("90000")
            mileagepage.confirm_car_mileage()

