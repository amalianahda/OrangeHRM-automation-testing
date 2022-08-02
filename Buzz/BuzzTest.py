import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
url="https://opensource-demo.orangehrmlive.com"
username="Admin"
password="admin123"

class Buzz(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(5)


    def test_Buzz_Status(self):
        driver = self.driver
        driver.get(url)
        time.sleep(5)
        self.login(driver)

        driver.find_element(By.ID, "menu_buzz_viewBuzz").click()
        time.sleep(0.5)
        driver.find_element(By.NAME, "createPost[content]").send_keys("Good Morning :)")
        time.sleep(0.5)
        driver.find_element(By.ID, "postSubmitBtn").click()
        time.sleep(2)
        
        status_posted = driver.find_elements(By.CSS_SELECTOR, ".postContent")

        for i in status_posted :
            if (i.text == status_posted) :
                self.assertEquals(i.text, status_posted)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()