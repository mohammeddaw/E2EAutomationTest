from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.Base_Page import BasePage


class HomePageForMotorWay(BasePage):
    # Locators

    textbox_EnterReg_xpath = "=//input[@id='vrm-input']"
    btn_ValueCar_xpath = ("//section[@class='HeroInput__container-JQKA HomepageVRM__heroInput-EYMF']//span[contains("
                          "text(),'Value your car')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self, url):
        #self.driver = webdriver.Chrome()
        self.driver.get(url)

    def enter_car_reg(self, car_reg_number):
        self.driver.find_element(By.XPATH(self.textbox_EnterReg_xpath)).clear()
        self.driver.find_element(By.XPATH(self.textbox_EnterReg_xpath)).send_keys(car_reg_number)

    def value_your_car(self):
        self.driver.find_element(By.XPATH(self.btn_ValueCar_xpath)).click()
