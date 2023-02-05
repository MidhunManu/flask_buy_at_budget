import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

def jio_mart_scraping(product_name):
  jio_url = f"https://www.jiomart.com/catalogsearch/result?q={product_name}"
  jio_url = jio_url.replace(" ", "+");
  data = []
  
  r = requests.get(jio_url, headers=headers)
  html_content = r.content
  soup = BeautifulSoup(html_content, "html.parser")
  
  price = soup.select("span#final_price")
  name = soup.select("span.clsgetname")
  link = soup.select("a.category_name.prod-name")
  
  for i in range(0, len(link)):
    data.append({"name":name[i].text, "price":price[i].text, "link":link[i].get("href"), "company":"Jio Mart"})

  return data