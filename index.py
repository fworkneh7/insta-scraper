from selenium import webdriver

DRIVER_PATH = "C:/Users/frazer/Downloads/chromedriver_win32/chromedriver.exe" #when working from your local server use your own chromedriver path
driver = webdriver.Chrome(DRIVER_PATH)
driver.get('https://www.instagram.com/p/CGQM1xdB5fW/')

i = 0
while i < 12:   # instagram only presents 12 comments at a time
    # append the comment to a list or write to a csv file
    i += 1
    if i == 12
        driver.find_element_by_xpath(#write in the xpath of the button).click()  #the click of this button is to add more comments 
        i - 12
    else:
        pass


   

