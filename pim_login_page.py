from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# from login_page import Orange
# class Orangepim:
#    def __init__(self, url):
#        self.url = url
#        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
#    def boot(self):
#        self.driver.get(self.url)
#        sleep(3)
#        self.driver.maximize_window()
#
#    def quit(self):
#        self.driver.quit()
#    def add_employee(self):
#        self.boot()
#        sleep(3)
#        self.driver.implicitly_wait = 60
#        username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
#
#        username.send_keys("Admin")
#        password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
#
#        password.send_keys("admin123")
#        login_button = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
#
#        login_button.click()
#        pim =self. driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
#        pim.click()
#        sleep(2)
#        add = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
#        add.click()
#        sleep(3)
#        employee_f_name=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
#
#        employee_f_name.send_keys("Shiva")
#        # #
#        sleep(3)
#        employee_m_name=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')
#        employee_m_name.send_keys("Rama")
#        sleep(3)
#        #
#        save2= self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click()
#        sleep(4)
#        print( "secessfully employee added !!!")
#        self.quit()
# obj = Orangepim("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# obj.add_employee()
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
        self.driver.implicitly_wait = 60
        username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')

        username.send_keys("Admin")
        password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')

        password.send_keys("admin123")
        login_button = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

        login_button.click()
        pim =self. driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        pim.click()
        sleep(2)

        self.driver.execute_script("window.scrollTo(500,500);")
        edit_employee_details = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[9]/div/button[2]').click()

        employe_f_name = WebDriverWait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input')))

        employe_f_name.send_keys("dev")
        sleep(1)
        employee_m_name = WebDriverWait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input')))

        employee_m_name.send_keys("a")
        employee_lname = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input')

        employee_lname.send_keys("s")
        emply_id = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input')

        emply_id.send_keys("571")
        other_id = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')

        other_id.send_keys("198")
        sleep(4)
        save = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click()

        sleep(4)
        print("secessfully employee added !!!")
        self.quit()


obj = orangepim2("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.edit_employee()

#


