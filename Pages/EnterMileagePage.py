from selenium.webdriver.common.by import By

from Pages.Base_Page import BasePage


class EnterMileagePage(BasePage):
    textbox_EnterRegMileage_xpath = "=//input[@id='mileage-input']"
    btn_ConfirmMileage_xpath = "//section[@class='HeroInput__container-JQKA HomepageVRM__heroInput-EYMF']//span[contains(text(),'Confirm mileage')]"

    def __init__(self, driver):
       super().__init__(driver)
       self.driver = driver


    def enter_car_mileage(self,car_mileage):
        self.driver.find_element(By.XPATH(self.textbox_EnterRegMileage_xpath)).clear()
        self.driver.find_element(By.XPATH(self.textbox_EnterRegMileage_xpath)).send_keys(car_mileage)
    def confirm_car_mileage(self):
        self.driver.find_element(By.XPATH(self.btn_ConfirmMileage_xpath)).click()