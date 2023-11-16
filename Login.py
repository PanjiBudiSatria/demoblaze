import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class LoginTest(unittest.TestCase):
    def setUp(self):
        chrome_driver_path = ChromeDriverManager().install()
        service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_a_success_login(self):
        self.driver.get("https://www.demoblaze.com/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,'nava')))
        self.driver.find_element(By.XPATH,'//*[@id="login2"]').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'loginusername')))

        self.driver.find_element(By.ID,'loginusername').send_keys('panjibuds')
        self.driver.find_element(By.ID,'loginpassword').send_keys('test123')
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]').click()
        time.sleep(5)

        self.assertEqual(self.driver.find_element(By.ID,'nameofuser').text,"Welcome panjibuds")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()