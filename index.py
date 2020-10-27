from selenium import webdriver

DRIVER_PATH = "C:/Users/frazer/Downloads/chromedriver_win32/chromedriver.exe"    #when working from your local server use your own chromedriver path
driver = webdriver.Chrome(DRIVER_PATH)
ig_path = driver.get('https://www.instagram.com/p/CGQM1xdB5fW/')

comment_list = []
i = 0
comment_count = 1
while i < 12:                 # instagram only presents 12 comments at a time
    comment_list.append(ig_path.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/div[1]/ul/ul['+ str(comment_count) +']/div/li/div/div/div[2]/span'))    # append the comment to a list or write to a csv file
    i += 1
    comment_count += 1
    if i == 12
        ig_path.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/div[1]/ul/li/div/button').click()  #the click of this button is to add more comments 
        i - 12
    else:
        pass