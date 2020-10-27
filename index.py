from selenium import webdriver

DRIVER_PATH = "C:/Users/frazer/Downloads/chromedriver_win32/chromedriver.exe" #when working from your local server use your own chromedriver path
driver = webdriver.Chrome(DRIVER_PATH)
driver.get('https://google.com')