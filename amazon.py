import os
import requests
import json
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

def amazon_scraping(product_name):
  
  amazon_product_name = product_name.replace(" ", "+")
  amazon_url = f"https://www.amazon.in/s?k={amazon_product_name}"
  data = []

  r = requests.get(amazon_url, headers=headers)
  htmlContent = r.content

  soup = BeautifulSoup(htmlContent, 'html.parser')
  prices = soup.find_all(class_="a-price-whole")
  # name = soup.find_all(class_="a-size-medium a-color-base a-text-normal")
  links = soup.find_all(class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
  images = soup.select("img.s-image")
  try:
    for i in range(0, len(links)):
      data.append({"names":product_name.replace("+"," "), "price":int(prices[i].text), "url":"https://www.amazon.in"+links[i].get("href"), "company":"amazon", "images":images[i].attrs.get("src")})
  except:
    pass
  
  return data
  # json_data = json.dumps(data)

  # with open("scrape.json", "w") as file:
  #     file.write(json.dumps(json_data))
 
  # os.system("node sortShoppingPrices.js")
    