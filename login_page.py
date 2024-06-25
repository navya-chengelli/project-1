from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Define a class for handling valid login on the OrangeHRM site
class Orange:
    def __init__(self, url):
        self.url = url
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        # Open the given URL
        self.driver.get(self.url)
        sleep(3)
        # Maximize the browser window
        self.driver.maximize_window()

    def quit(self):
        # Quit the driver
        self.driver.quit()

    def valid_login(self):
        # Start the browser and open the URL
        self.boot()
        sleep(3)
        # Find the username field and enter the username
        username = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username.send_keys("Admin")
        # Find the password field and enter the password
        password = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password.send_keys("admin123")
        # Find the login button and click it
        login_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        login_button.click()
        print("User is logged in successfully !!!")
        sleep(3)
        # Quit the driver
        self.quit()

# Create an instance of Orange and perform a valid login
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.valid_login()

# Define a class for handling invalid login on the OrangeHRM site
class Orangehrm:
    def __init__(self, url):
        self.url = url
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        # Open the given URL
        self.driver.get(self.url)
        sleep(3)
        # Maximize the browser window
        self.driver.maximize_window()

    def quit(self):
        # Quit the driver
        self.driver.quit()

    def invalid_login(self):
        # Start the browser and open the URL
        self.boot()
        sleep(3)
        # Find the username field and enter the username
        username = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username.send_keys("Admin")
        # Find the password field and enter an incorrect password
        password = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password.send_keys("dmin123")
        # Find the login button and click it
        login_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        login_button.click()
        print("Invalid credentials!!!")
        sleep(3)
        # Quit the driver
        self.quit()

# Create an instance of Orangehrm and perform an invalid login
obj = Orangehrm("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.invalid_login()

