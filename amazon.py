import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

def amazon_scraping(product_name):
  amazon_product_name = product_name.replace(" ", "+")
  amazon_url = f"https://www.amazon.in/s?k={amazon_product_name}"
  data = []
  result = {}

  r = requests.get(amazon_url, headers=headers)
  html_content = r.content
  
  soup = BeautifulSoup(html_content, "html.parser")
  prices = soup.find_all(class_="a-price-whole")
  ratings = soup.find_all(class_="a-icon-alt")
  names = product_name
  links = soup.find_all(class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
  
  try:
    for i in range(0, 10):
      data.append({"names":names, "price":prices[i].text, "url":"https://www.amazon.in"+links[i].get("href"), "company":"amazon"})
  except:
    pass
    
  amazon_json_data = data
  return amazon_json_data