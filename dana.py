import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.olx.ua/d/obyavlenie/besprovodnye-naushniki-airpods-pro-tws-macaron-garantiya-IDIIExT.html'

req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
loka = soup.find("p", class_="css-7xdcwc-Text eu5v0x0").text
print(loka)