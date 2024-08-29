from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #If the chrome driver closes automatically this code will help
driver = webdriver.Chrome(options=options)

driver.get("http://www.tcs.com")
driver.maximize_window()
print(driver.title)

driver.close()