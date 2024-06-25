from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
class Orange:
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(self.url)
       sleep(3)
       self.driver.maximize_window()

   def quit(self):
       self.driver.quit()

   def valid_login(self):
       self.boot()
       sleep(3)
       username=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
       username.send_keys("Admin")
       password=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
       password.send_keys("admin123")
       login_button=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
       login_button.click()
       print("User is logged in successfully !!!")
       sleep(3)
       self.quit()

obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.valid_login()
class Orangehrm:
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(self.url)
       sleep(3)
       self.driver.maximize_window()

   def quit(self):
       self.driver.quit()
   def invalid_login(self):
        self.boot()
        sleep(3)
        username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')

        username.send_keys("Admin")
        password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password.send_keys("dmin123")
        login_button = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

        login_button.click()
        print("Invalid credentials!!!")
        sleep(3)

        self.quit()



obj = Orangehrm("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

obj.invalid_login()


