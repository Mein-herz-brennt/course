from bs4 import BeautifulSoup
import requests

req = requests.get("https://avias.ua/karta-azs/?region_id=3")
req2 = requests.post("https://avias.ua/karta-azs/?region_id=3",
                     data={
                         "a": "true"})
print(req2.text)

soup = BeautifulSoup(req2.text, "lxml")
all_tr = soup.find("a", class_="op-azs")

print(all_tr)
