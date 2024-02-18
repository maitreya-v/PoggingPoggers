from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("https://www.zomato.com/mumbai/ettarra-1-juhu/order")
# import openpyxl

# Create a new workbook
# workbook = openpyxl.Workbook()

# Get the active worksheet
# worksheet = workbook.active

# Write the headers
# worksheet['A1'] = 'Names'
# worksheet['B1'] = 'Prices'
# worksheet['C1'] = 'Stars'
# worksheet['D1'] = 'Votes'
# worksheet['E1'] = 'Description'
# worksheet['F1'] = 'Image Source'
# whole_section =  driver.find_elements(By.CLASS_NAME, 'sc-cxZfpC.gnKHwi')
# different_sections = []
# for section in whole_section:
#     print

# combos = driver.find_element(By.CLASS_NAME,'sc-lmrgJh.gfKczc')
# # all_divs = combos.find_elements(By.TAG_NAME,'div')

# names_combo = []
# prices = []
# all_divs = combos.find_elements(By.TAG_NAME,'div')
# first_div = []
# for num,div in enumerate(all_divs):
#     if num%6==0:
#         print(div.text)

# # for num,i in enumerate(first_div):
    
# # for div in all_div    s:
#     # print(div.text)

time.sleep(60)
# print("end")
divs = driver.find_elements(By.CLASS_NAME,'sc-1s0saks-10.cYSFTJ')
# read_more = driver.find_elements(By.CLASS_NAME,'sc-ya2zuu-0.SWRrQ')
# for x in read_more:
#     x.click()
#     time.sleep(1)
# for name in names:
#     print(name.text)
# print(len(names))
# # print(len(names))
# print("end")
names = []
prices = []
stars = []
votes = []
description = []
for num,div in enumerate(divs):
    try:
        names.append(div.find_element(By.CLASS_NAME,'sc-1s0saks-15.iSmBPS').text)
    except:
        names.append("NAN")
        print("name not there for div number {}".format(num))
    try:
        prices.append(div.find_element(By.CLASS_NAME,'sc-17hyc2s-1.cCiQWA').text)
    except:
        prices.append("NAN")
        print("price not there for div number {}".format(num))
    try:
        stars.append(div.find_element(By.CLASS_NAME,'sc-17hyc2s-1.cCiQWA').text)
    except:
        stars.append("NAN")
        print("stars not there for div number {}".format(num))
    try:
        votes.append(div.find_element(By.CLASS_NAME,'sc-z30xqq-4.hTgtKb').text)
    except:
        votes.append("NAN")
        print("votes not there for div number {}".format(num))
    
    try:
        description.append(div.find_element(By.CLASS_NAME,'sc-1s0saks-12.hcROsL').text)
    except:
        description.append("NAN")
        print("description not there for div number {}".format(num))
    
    # try:
    #     src = div.find_element(By.CLASS_NAME,'sc-s1isp7-5.fyZwWD').get_attribute("src")
    #     image_src.append(src)
    # except:
    #     image_src.append("NAN")
    #     print("image not there for div number {}".format(num))
    
    
all_imgs = driver.find_elements(By.TAG_NAME,'img')
image_src = []
for name in names:
    flag = False
    for img in all_imgs:
        if img.get_attribute("alt") == name:
            image_src.append(img.get_attribute("src"))
            flag = True
            break
    if flag==False:
        image_src.append("NAN")
    
    
    
print(len(names))
print(len(prices))
print(len(stars))
print(len(votes))
print(len(description))
    
# row = 2
# for i in range(len(names)):
#     worksheet.cell(row=row, column=1, value=names[i])
#     worksheet.cell(row=row, column=2, value=prices[i])
#     worksheet.cell(row=row, column=3, value=stars[i])
#     worksheet.cell(row=row, column=4, value=votes[i])
#     worksheet.cell(row=row, column=5, value=description[i])
#     worksheet.cell(row=row, column=6, value=image_src[i])
#     row += 1

import pandas as pd

# Create a dictionary with the data
data = {
    'Names': names,
    'Prices': prices,
    'Stars': stars,
    'Votes': votes,
    'Description': description,
    'Image Source': image_src
}

# Create a DataFrame
df = pd.DataFrame(data)

# Write to an Excel file
df.to_excel('data.xlsx', index=False)
# Save the workbook
# workbook.save('data.xlsx')