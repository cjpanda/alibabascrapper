# Import Selenium, Time and By 
from textwrap import indent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time

# options= Options()
# options.add_argument("--headless")

chrome_path = (r"C:\Users\90533\Desktop\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(chrome_path)
# geth the page url you want to scrapp 
driver.get ('https://www.alibaba.com/products/plain_tshirts_for_printing.html') 
time.sleep(1)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

items = driver.find_elements(By.CSS_SELECTOR, ".J-offer-wrapper")

output = []

# iterate through tthe items on the page 
for i in items:
    try:
        product_name = i.find_element(By.CSS_SELECTOR, ".elements-title-normal__outter").text
    except:
        product_name = None
    try:
        price = i.find_element(By.CSS_SELECTOR, ".elements-offer-price-normal").text
    except:
        price = None
    try:
        moq = i.find_element(By.CSS_SELECTOR, ".element-offer-minorder-normal__value").text
    except:
        moq = None
    try: 
        img_div = i.find_element(By.CSS_SELECTOR, ".seb-img-switcher__imgs")
        img_url = img_div.get_attribute("data-image")
        img_url = "https:" + img_url
        img_url = img_url.replace("_300x300.jpg", "")
    except:
        img_url = None 

    output_item = {"Product Name": product_name, "Price": price, "MOQ": moq, "Image Url": img_url}
    output.append(output_item)

json.dump(output, open("alibaba.json", "w"), indent = 2)
    # print(price,"|", product_name,"|", moq, "|", img_url)
print("Done and saved")


driver.close()


