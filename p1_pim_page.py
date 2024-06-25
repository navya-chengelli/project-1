from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Orangepim:
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

    def add_employee(self):
        # Start the browser and open the URL
        self.boot()
        sleep(3)
        # Set an implicit wait
        self.driver.implicitly_wait = 60
        # Find the username field and enter the username
        username = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username.send_keys("Admin")
        # Find the password field and enter the password
        password = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password.send_keys("admin123")
        # Find the login button and click it
        login_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        login_button.click()
        sleep(2)
        # Navigate to the PIM section
        pim = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        pim.click()
        sleep(2)
        # Find and click the 'Add' button to add a new employee
        add = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        add.click()
        sleep(3)
        # Fill in the employee's first name
        employee_f_name = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
        employee_f_name.send_keys("Shiva")
        sleep(3)
        # Fill in the employee's middle name
        employee_m_name = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')
        employee_m_name.send_keys("Rama")
        sleep(3)
        # Fill in the employee's last name
        employee_l_name = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
        employee_l_name.send_keys("Shiva")
        sleep(3)
        # Fill in the employee ID
        emply_id = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
        emply_id.send_keys("571")
        sleep(2)
        # Find and click the 'Save' button
        save = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
        save.click()
        sleep(4)
        # Print success message
        print("Successful employee added !!!")
        sleep(2)
        # Quit the driver
        self.quit()

# Create an instance of Orangepim and add an employee
obj = Orangepim("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.add_employee()

class orangepim3:
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

    def delete_employee(self):
        # Start the browser and open the URL
        self.boot()
        sleep(3)
        # Set an implicit wait
        self.driver.implicitly_wait = 60
        # Find the username field and enter the username
        username = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username.send_keys("Admin")
        # Find the password field and enter the password
        password = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password.send_keys("admin123")
        # Find the login button and click it
        login_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        login_button.click()
        sleep(2)
        # Navigate to the PIM section
        pim = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        pim.click()
        sleep(2)
        # Scroll down to the employee list
        self.driver.execute_script("window.scrollTo(500,500);")
        sleep(2)
        # Find and click the delete button for the specific employee
        delete_the_data = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]')
        delete_the_data.click()
        sleep(2)
        # Confirm deletion
        delete = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
        delete.click()
        sleep(2)
        # Print success message
        print("Successful deletion !!!")
        sleep(2)
        # Quit the driver
        self.quit()

# Create an instance of orangepim3 and delete an employee
obj = orangepim3("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.delete_employee()

class orangepim2:
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

    def edit_employee(self):
        # Start the browser and open the URL
        self.boot()
        sleep(3)
        # Set an implicit wait
        self.driver.implicitly_wait = 60
        # Find the username field and enter the username
        username = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username.send_keys("Admin")
        # Find the password field and enter the password
        password = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password.send_keys("admin123")
        # Find the login button and click it
        login_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        sleep(2)
        login_button.click()
        sleep(2)
        # Navigate to the PIM section
        pim = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        sleep(2)
        pim.click()
        sleep(2)
        # Scroll down to the employee list
        self.driver.execute_script("window.scrollTo(500,500);")
        sleep(2)
        # Find and click the edit button for the specific employee

        edit_employee_details = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[6]/div/button[2]')


        sleep(2)
        edit_employee_details.click()
        sleep(2)
        username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input')

        sleep(2)
        username.send_keys("ram")
        sleep(2)

        save = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
        sleep(2)
        save.click()

        sleep(4)
        print("successfully employee edited  !!!")
        sleep(2)
        self.quit()


    obj = orangepim2("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    obj.edit_employee()