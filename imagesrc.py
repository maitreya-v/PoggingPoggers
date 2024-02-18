from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
num = 1
link = "https://www.zomato.com/mumbai/ettarra-1-juhu/reviews?page={}&sort=dd&filter=reviews-dd".format(num)
driver.get(link)

while True:
    time.sleep(2)
    num+=1
    driver.quit()
    options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    new_link = "https://www.zomato.com/mumbai/ettarra-1-juhu/reviews?page={}&sort=dd&filter=reviews-dd".format(str(num))
    driver.get(new_link)
    # next_btn = driver.find_element(By.CLASS_NAME, 'sc-boCWhm.sc-cIsjWt.sc-OnmeF.hupwEE')
    # next_btn.click()
    # time.sleep(2)
    # print(len(next_btn))
# time.sleep(1)