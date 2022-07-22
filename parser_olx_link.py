import requests
from bs4 import BeautifulSoup
import aiohttp


def get_desk():
    seshion = aiohttp.ClientSession()
    seshion.post(f'https://www.olx.pl/api/v1/offers/740460809/page-views/',
                            headers={'Authorization': "Bearer af71501ae28c1acf1d6da52f92bb5ba48904e90e"})
    return d


# print(get_number("https://www.olx.ua/d/obyavlenie/remeshok-braslet-apple-watch-applewatch-iwatch-epl-votch-38-40-42"
#                  "-44-IDHFmu2.html"))

def get_views(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    div = soup.find("div", class_="css-1ferwkx")  # .find_all("span")
    print(div)


print(get_desk())
