import requests
from bs4 import BeautifulSoup

link = "https://chinabazaar.olx.ua/#contact"

headers = {
    'Authorization': "Bearer f2e37f1f961e558e71bed60a9c6058477e790043",
    'Accept': '*/*',
    'Host': 'www.olx.ua',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode    ': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}

req = requests.get(link, headers=headers)

with open("olx.html", "wb") as f:
    f.write(req.content)
soup = BeautifulSoup(req.text, "lxml")

phone = soup.find("ul", class_='css-1ooq9gg').find('li').contents
print(phone)