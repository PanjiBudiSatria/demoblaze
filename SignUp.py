import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class SignUpTest(unittest.TestCase):
    def setUp(self):
        chrome_driver_path = ChromeDriverManager().install()
        service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_a_success_signup(self):
        #Navigate to Login Form
        self.driver.get("https://www.demoblaze.com/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,'nava')))
        self.driver.find_element(By.ID,'signin2').click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,'signInModalLabel')))

        #Signup Process
        self.driver.find_element(By.ID,'sign-username').send_keys('panjibuds')
        self.driver.find_element(By.ID,'sign-password').send_keys('test123')
        self.driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[3]/button[2]')

        #Asserting the success alert
        try :
            alert = self.driver.switch_to.alert
            assert "Sign up successful." in alert.text
            alert.accept()
        except:
            print("No alert present")
        
        self.assertTrue(self.driver.find_element(By.ID,'nava').text,"PRODUCT STORE")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()