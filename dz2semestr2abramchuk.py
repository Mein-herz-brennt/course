from bs4 import BeautifulSoup
import requests
import datetime

req = requests.session().get("https://pogoda.org.ua/kiev", headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"})

soup = BeautifulSoup(req.text, "lxml")
current_time = datetime.datetime.now().time()
time_from_site = soup.find("span", id="clock").text

list_time = time_from_site.split(":")

if int(list_time[0]) == current_time.hour and int(list_time[1]) == current_time.minute and int(list_time[2]) == current_time.second:
    print("Час на сайті та на комп'ютері співпадає")
else:
    print(f"Час не співпав на {current_time.second - int(list_time[2])} секунд(у)")

print("Час з сайту" + " - " + time_from_site)
print("Час на комп'ютері" + " - " + str(current_time))
