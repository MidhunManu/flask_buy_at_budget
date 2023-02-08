import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

def jio_mart_scraping(product_name):
  jio_url = f"https://www.jiomart.com/catalogsearch/result?q={product_name}"
  jio_url = jio_url.replace(" ", "%20");
  data = []
  
  r = requests.get(jio_url, headers=headers)
  html_content = r.content
  soup = BeautifulSoup(html_content, "html.parser")
  
  price = soup.select("span#final_price")
  name = soup.find_all(class_="clsgetname")
  link = soup.find_all(class_="category_name prod-name")
  
  try:
    for i in range(0, len(link)):
      data.append({"name":name[i].text,
                   "price":price[i].text,
                   "link":link[i].get("href"),
                   "company":"Jio Mart"})
  except:
    pass
  return data