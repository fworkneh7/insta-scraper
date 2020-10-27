from selenium import webdriver

DRIVER_PATH = "C:/Users/frazer/Downloads/chromedriver_win32/chromedriver.exe" #when working from your local server use your own chromedriver path
driver = webdriver.Chrome(DRIVER_PATH)
driver.get('https://www.instagram.com/p/CGQM1xdB5fW/')


path = r"C:/Users/frazer/OneDrive/Documents/GitHub/assignment-1/insta-scraper/script.csv"


i = 0
while i < 12:   # instagram only presents 12 comments at a time
  # append the comment to a list or write to a csv file
  i += 1
  if i == 12
    #click button to add more comments 
    i - 12

   

