import json
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def load_config(context):

        try:
            with open("TestData/TestConfiguration.json", "r") as jsonfile:
                data = json.load(jsonfile)  # Reading the file
                print("Read successful")
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at TestData/TestConfiguration.json")

        def before_scenario(context, scenario):
            # Setup Chrome options
            chrome_options = Options()
            if context.config.get('headless', False):
                chrome_options.add_argument('--headless')

            # Initialize WebDriver
            context.driver = webdriver.Chrome(options=chrome_options)
            context.driver.maximize_window()
            context.driver.get("https://motorway.co.uk/")


    def before_all(context):
        # Load configuration
        context.config = context.load_config()

        # Initialize page objects dictionary
        context.pages = {}



    def setup_driver(context):
        """Initialize WebDriver"""
        context.driver = webdriver.Chrome()  # Add your driver configuration here
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)

    def initialize_page_objects(context):
        """Initialize all page objects"""

       # Add current_page attribute to track the current page
        context.current_page = None

    def after_scenario(context, scenario):
        """Cleanup after scenario"""
        if hasattr(context, 'driver'):
            context.driver.quit()
    def setup_driver(context):
        """Initialize WebDriver"""
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')

        # Initialize the driver using webdriver manager
        context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                          options=chrome_options)
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)

