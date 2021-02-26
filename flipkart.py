from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

laptops = []

for x in range(1, 31):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63'}
    url = 'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='

    uclient = requests.get(url + str(x), headers = headers).text
    soup = BeautifulSoup(uclient, 'lxml')
    product_content = soup.find_all('div', class_ = '_3pLy-c row')
    for product in product_content:
        product_name = product.find('div', class_ = '_4rR01T').text
        product_feature = product.find('ul', class_ = '_1xgFaf').text
        product_price = product.find('div', class_ = '_30jeq3 _1_WHN1').text

        product_info = {
            'Name' : product_name,
            'Feature' : product_feature,
            'Price' : product_price
        }
        laptops.append(product_info)
    time.sleep(2)

df = pd.DataFrame(laptops)
df.to_csv('laptops.csv')