from sys import executable

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementById():
    def locate_by_id_demo(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # If the chrome driver closes automatically this code will help
        driver = webdriver.Chrome(options=options)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        #Find the element by ID
        driver.find_element("id", "login-input").send_keys("Test@Test.com")

findById = DemoFindElementById()
findById.locate_by_id_demo()
