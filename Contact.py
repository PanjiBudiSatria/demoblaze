import unittest
import time
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Login import LoginTest

class ContactTest(unittest.TestCase):

    def setUp(self):
        self.login_method = LoginTest()
        self.login_method.setUp()
        self.login_method.test_a_success_login()
        self.driver_from_login = self.login_method.get_driver()

    def test_a_move_to_contact_form(self):
        WebDriverWait(self.driver_from_login, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/nav/div[1]/ul/li[2]/a"))).click()

        # Wait for the modal to be present
        WebDriverWait(self.driver_from_login, 10).until(
            EC.presence_of_element_located((By.ID, "recipient-email"))
        )

        # Scroll into view if needed
        # element = driver_from_login.find_element(By.ID, "recipient-email")
        # driver_from_login.execute_script("arguments[0].scrollIntoView();", element)

        # Wait for the element to be clickable
        WebDriverWait(self.driver_from_login, 10).until(
            EC.element_to_be_clickable((By.ID, "recipient-email"))
        ).send_keys("panjibudi467@gmail.com")

        self.driver_from_login.find_element(By.ID, "recipient-name").send_keys("Panji Budi Satria")
        self.driver_from_login.find_element(By.ID, "message-text").send_keys("ini adalah testing message pada menu contact")
        self.driver_from_login.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]").click()

        try:
            alert = self.driver_from_login.switch_to.alert
            assert "Thanks for the message!!" in alert.text
            alert.accept()
            time.sleep(3)
        except:
            print("No alert present")

        self.assertEqual(self.driver_from_login.find_element(By.ID, 'nameofuser').text, "Welcome panjibuds")

    def tearDown(self):
        self.login_method.tearDown()

if __name__ == "__main__":
    unittest.main(argv=sys.argv + ['ContactTest'])