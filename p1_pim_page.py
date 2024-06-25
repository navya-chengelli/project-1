from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from login_page import Orange
class Orangepim:
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(self.url)
       sleep(3)
       self.driver.maximize_window()

   def quit(self):
       self.driver.quit()
   def add_employee(self):
       self.boot()
       sleep(3)
       self.driver.implicitly_wait = 60
       username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')

       username.send_keys("Admin")
       password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')

       password.send_keys("admin123")
       login_button = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

       login_button.click()
       sleep(2)
       pim =self. driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
       sleep(2)
       pim.click()
       sleep(2)
       add = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
       sleep(2)
       add.click()
       sleep(3)
       employee_f_name=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
       sleep(2)
       employee_f_name.send_keys("Shiva")
#
       sleep(3)
       employee_m_name=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')
       sleep(2)
       employee_m_name.send_keys("Rama")
       sleep(3)
       employee_l_name = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
       sleep(3)
       employee_l_name.send_keys("Shiva")
       sleep(3)
       emply_id = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
       sleep(2)
       emply_id.send_keys("571")
       sleep(2)
       save= self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
       sleep(2)
       save.click()
       sleep(4)
       print("sucessful employee added !!!")
       sleep(2)
       self.quit()
obj = Orangepim("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.add_employee()
class orangepim3:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def delete_employee(self):
        self.boot()
        sleep(3)
        self.driver.implicitly_wait = 60
        username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')


        username.send_keys("Admin")
        password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')


        password.send_keys("admin123")
        login_button = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')


        login_button.click()
        sleep(2)
        pim = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        sleep(2)
        pim.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(500,500);")
        delete_the_data =self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]')
        sleep(2)
        delete_the_data.click()

        sleep(2)
        delete=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
        delete.click()
        sleep(2)
        print("successful deletion !!!")
        sleep(2)
        self.quit()

obj = orangepim3("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.delete_employee()

class orangepim2:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()
    def edit_employee(self):
        self.boot()
        sleep(3)

        self.driver.implicitly_wait = 60
        username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')

        username.send_keys("Admin")
        password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')

        password.send_keys("admin123")
        login_button = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        sleep(2)
        login_button.click()
        sleep(2)
        pim = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        sleep(2)
        pim.click()
        sleep(2)

        self.driver.execute_script("window.scrollTo(500,500);")
        sleep(2)
        edit_employee_details = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[6]/div/button[2]')

        sleep(2)
        edit_employee_details.click()
        sleep(2)
        username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input')

        sleep(2)
        username.send_keys("ram")
        sleep(2)
        # other_id = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')
        #
        # other_id.send_keys("198")
        # sleep(4)
        save = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
        sleep(2)
        save.click()

        sleep(4)
        print("successfully employee edited  !!!")
        sleep(2)
        self.quit()


obj = orangepim2("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.edit_employee()






#


