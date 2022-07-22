import requests
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/_brennendes_herz_/'


def get_name(url: str):
    response = requests.get(url)
    soap = BeautifulSoup(response.text, 'lxml')
    nic = soap.find(class_="v9tJq AAaSh VfzDr")
    nick = soap.find_all('h2')
    return nic


print(get_name(url))
