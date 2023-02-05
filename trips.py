import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

def trips_scraping(start_location, end_location, departure_day):
  departure_day = departure_day.split("-");
  year = departure_day[0];
  month = departure_day[1];
  day = departure_day[2];
  date = f"{year}/{month}/{day}"
  
  trips_url = f"https://www.google.com/search?q=cheapest+flight+from+{start_location}+to+{end_location}+on+{date}&oq=cheapest+flight+from+{start_location}+to+${end_location}&aqs=chrome..69i57.11745j0j4&sourceid=chrome&ie=UTF-8"
  r = requests.get(trips_url, headers=headers)
  html_content = r.content
  
  
  soup = BeautifulSoup(html_content, "html.parser")
  airline = soup.select("span.ps0VMc")
  duration = soup.find_all(class_="sRcB8")
  price = soup.select("span.GARawf")
  stops = soup.find_all(class_="u85UCd")
  link = soup.select("div.YXEKBb.LQQ1Bd > div > div > a")
  
  data = []
  
  try:
    for i in range(0, len(price)):
      data.append({"airline":airline[i].text,
                   "duration":duration[i].text,
                   "price":price[i].text,
                   "stops":stops[i].text,
                   "url":link[i].get("href")
                   })
  except:
    pass
  
  return data
  