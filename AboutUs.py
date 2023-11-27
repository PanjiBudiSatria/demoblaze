import unittest
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Login import LoginTest

class AboutUsTest(unittest.TestCase):

    def setUp(self):
        self.login_method = LoginTest()
        self.login_method.setUp()
        self.login_method.test_a_success_login()
        self.driver_from_login = self.login_method.get_driver()

    def test_a_open_about_us(self):
        WebDriverWait(self.driver_from_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/nav/div[1]/ul/li[3]/a"))
        ).click()

        WebDriverWait(self.driver_from_login, 10).until(
            EC.presence_of_element_located((By.ID, "videoModalLabel"))
        )

        # Use JavaScript click to handle ElementClickInterceptedException
        video_element = WebDriverWait(self.driver_from_login, 10).until(
            EC.element_to_be_clickable((By.ID, "example-video_html5_api"))
        )
        self.driver_from_login.execute_script("arguments[0].click();", video_element)

        # Use ActionChains to play the video
        actions = ActionChains(self.driver_from_login)
        actions.move_to_element(video_element).click().perform()

        # Wait for the video to play for 10 seconds
        time.sleep(10)

        # Pause the video using JavaScript
        self.driver_from_login.execute_script("arguments[0].pause();", video_element)

        WebDriverWait(self.driver_from_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[3]/button"))
        ).click()

        time.sleep(1)
        self.assertEqual(self.driver_from_login.find_element(By.ID, 'nameofuser').text, "Welcome panjibuds")

    def tearDown(self):
        self.login_method.tearDown()

if __name__ == "__main__":
    unittest.main(argv=sys.argv + ['AboutUsTest'])
