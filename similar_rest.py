from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
# driver.get("https://www.zomato.com/mumbai/ettarra-1-juhu/order")

restaurant_list = ["Ettarra","Ananda Cafe","Third Wave Coffee", "Javaphile","Earth Cafe @ Juhu","Love & Latte"]

link_list = ["https://www.zomato.com/mumbai/ettarra-1-juhu","https://www.zomato.com/mumbai/ananda-cafe-juhu","https://www.zomato.com/mumbai/third-wave-coffee-juhu","https://www.zomato.com/mumbai/javaphile-pali-hill-bandra-west","https://www.zomato.com/mumbai/earth-cafe-@-juhu-1-juhu","https://www.zomato.com/mumbai/love-latte-juhu"]

cuisines = []
popular_dishes = []
known_for = []
average_cost = []
more_info = []
review_highlights = []

for link in link_list:
    driver.get(link)
    time.sleep(3)
    # cuisines.append(driver.find_elements(By.CLASS_NAME,'sc-fgfRvd.gBMRZZ')
# print(cuisines)
    anchors = driver.find_elements(By.CLASS_NAME,'sc-eKQksS.bKSGgJ')
    anchor_string = ""jmhumhyug
    for anchor in anchors:
        anchor_string = anchor_string + anchor.text + ","
    anchor_string = anchor_string[:-1]
    cuisines.append(anchor_string)
    
    dishes = driver.find_element(By.CLASS_NAME,'sc-1hez2tp-0.sc-dRFBHB.gjUzYI').text
    popular_dishes.append(dishes)
    
    known_for.append(driver.find_elements(By.CLASS_NAME,'sc-1hez2tp-0.sc-dRFBHB.gjUzYI')[1].text)
    
    average_cost.append(driver.find_elements(By.CLASS_NAME,'sc-1hez2tp-0.sc-dRFBHB.gjUzYI')[2].text)    
    
    info_tags = driver.find_elements(By.CLASS_NAME,'sc-1hez2tp-0.cunMUz')
    info_anchor = ""
    for info_tag in info_tags:
        info_anchor = info_anchor + info_tag.text + ","
    info_anchor = info_anchor[:-1]
    more_info.append(info_anchor)
    
    # review_string = ""
    # review = driver.find_elements(By.CLASS_NAME,'sc-eqGige.sc-dDojKJ.irlsVZ')
    # print(len(review))
    # for x in review:
    #     review_string = review_string + x.text + ","
    # review_string = review_string[:-1]
    # review_highlights.append(review_string)
    

print(cuisines)
print(popular_dishes)
print(known_for)
print(average_cost)
print(more_info)
# print(review_highlights)
print(restaurant_list)
    

import pandas as pd

# Create a dictionary with the data
data = {
    'Restaurant': restaurant_list,
    'Cuisines': cuisines,
    'Popular Dishes': popular_dishes,
    'Known For': known_for,
    'Average Cost': average_cost,
    'More Info': more_info,
    # 'Review Highlights': review_highlights
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_csv('restaurant_data.csv', index=False)    

