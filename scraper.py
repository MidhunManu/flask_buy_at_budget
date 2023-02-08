import requests
from bs4 import BeautifulSoup
from json import dumps

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
product_name = input("enter product name : ")
product_name = product_name.replace(" ", "+")
url = f"https://www.amazon.in/s?k={product_name}"
data = []

r = requests.get(url, headers=headers)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')
prices = soup.find_all(class_="a-price-whole")
name = soup.find_all(class_="a-size-medium a-color-base a-text-normal")
links = soup.find_all(class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
# images = soup.find("div", {"class":"a-section aok-relative s-image-tall-aspect"}).findChildren("img")
images = soup.select("img.s-image")

for i in images:
    print(i.attrs.get("src"))
    


for i in range(0, 10):
    try:
        data.append({"price":int(prices[i].text), "url":"https://www.amazon.in"+links[i].get("href"), "image":images[i].attrs.get("src")})
    except:
        pass

json_data = dumps(data)

with open("scrape.json", "w") as file:
    file.write(json_data)
 
