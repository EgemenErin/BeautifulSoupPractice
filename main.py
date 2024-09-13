from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl

response = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")
website = response.text

soup = BeautifulSoup(website, "html.parser")

goods = soup.findAll("a", {"class": "title"})
prices = soup.findAll("h4", {"class": "price float-end card-title pull-right"})
good_names = [good.get_text() for good in goods]
price_values = [price.get_text() for price in prices]
data = pd.DataFrame({
    'Product': good_names,
    'Price': price_values
})
data.to_excel('products.xlsx', index=False)