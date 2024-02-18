# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(options=options)
# driver.get("https://www.zomato.com/mumbai/ettarra-1-juhu/reviews")

# next_btn = driver.find_element(By.CLASS_NAME,'sc-rbbb40-0.iRDDBk')

# while next_btn:
#     rating = []
#     review = []
#     timestamp  = []
#     delivery_din = []
#     all_ratings = driver.find_elements(By.CLASS_NAME,'sc-1q7bklc-1.cILgox')[2:7]
#     reviews = driver.find_elements(By.CLASS_NAME,'sc-1hez2tp-0.sc-csZoYU.dJxGwQ')
#     timestamps = driver.find_elements(By.CLASS_NAME,'sc-1hez2tp-0.fKvqMN.time-stamp')
#     delivery_dining = driver.find_elements(By.CLASS_NAME,'sc-1q7bklc-9.dYrjiw')

#     for x in all_ratings:
#         rating.append(x.text)

#     for x in reviews:
#         review.append(x.text)

#     for x in timestamps:
#         timestamp.append(x.text)

#     for x in delivery_dining:
#         delivery_din.append(x.text)
        
#     print(rating)
#     print(review)
#     print(timestamp)
#     print(delivery_din)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("https://www.zomato.com/mumbai/tim-hortons-linking-road-bandra-west/reviews")

# Create an empty DataFrame to store the data
reviews_df = pd.DataFrame(columns=['Rating', 'Review', 'Timestamp', 'Delivery/Dining'])

next_btn = driver.find_element(By.CLASS_NAME, 'sc-rbbb40-0.iRDDBk')
num = 1
link = "https://www.zomato.com/mumbai/tim-hortons-linking-road-bandra-west/reviews?page={}&sort=dd&filter=reviews-dd".format(str(num))
rating = []
review = []
timestamp = []
delivery_din = []

while num!=43:
    
    all_ratings = driver.find_elements(By.CLASS_NAME, 'sc-1q7bklc-1.cILgox')[2:7]
    reviews = driver.find_elements(By.CLASS_NAME, 'sc-1hez2tp-0.sc-csZoYU.dJxGwQ')
    timestamps = driver.find_elements(By.CLASS_NAME, 'sc-1hez2tp-0.fKvqMN.time-stamp')
    delivery_dining = driver.find_elements(By.CLASS_NAME, 'sc-1q7bklc-9.dYrjiw')

    for x in all_ratings:
        rating.append(x.text)

    for x in reviews:
        if x.text=="":
            review.append("NAN")
        else:
            review.append(x.text)

    for x in timestamps:
        timestamp.append(x.text)

    for x in delivery_dining:
        delivery_din.append(x.text)
    print(num)
    # temp_df = pd.DataFrame({'Rating': rating, 'Review': review, 'Timestamp': timestamp, 'Delivery/Dining': delivery_din})
    # reviews_df = pd.concat([reviews_df, temp_df], ignore_index=True)
    # print(temp_df)
    try:
#         driver.exit()
#         num+=1
#         options = webdriver.FirefoxOptions()
#         driver = webdriver.Firefox(options=options)
# # driver.get("https://www.zomato.com/mumbai/ettarra-1-juhu/reviews")
#         link = "https://www.zomato.com/mumbai/ettarra-1-juhu/reviews?page={}&sort=dd&filter=reviews-dd".format(num)
#         time.sleep(2)
#         driver.get(link)
        time.sleep(1)
        num+=1
        driver.quit()
        options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        new_link = "https://www.zomato.com/mumbai/tim-hortons-linking-road-bandra-west/reviews?page={}&sort=dd&filter=reviews-dd".format(str(num))
        driver.get(new_link)
    except:
        break

import pandas as pd

min_num = min(len(delivery_din),len(review),len(timestamp),len(rating))
rating = rating[:min_num]
delivery_din = delivery_din[:min_num]
timestamp = timestamp[:min_num]
review = review[:min_num]
# Create a dictionary with the data
data = {
    'Rating': rating,
    'Reviews': review,
    'Timestamp': timestamp,
    'Delivery/Dining': delivery_din,
}

# Create a DataFrame
df = pd.DataFrame(data)

# Write to an Excel file
df.to_csv('tim_hortons_review.csv', index=False)

# driver.quit()

# reviews_df.to_csv('reviews.csv', index=False)