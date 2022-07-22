import requests
from bs4 import BeautifulSoup
import datetime

req = requests.get("https://www.timeanddate.com/worldclock/ukraine/kyiv")
soup = BeautifulSoup(req.text, "html.parser")

current_time_in_site = soup.find("span", id="ct", class_="h1").text
list_time = current_time_in_site.split(":")

current_time_in_laptop = datetime.datetime.now().time()

if int(list_time[0]) == current_time_in_laptop.hour and int(list_time[1]) == current_time_in_laptop.minute and int(list_time[2]) == current_time_in_laptop.second:
    print("Час на сайті та на комп'ютері співпадає")
else:
    print(f"Час не співпав на {current_time_in_laptop.second - int(list_time[2])} секунд(у)")

print("Час з сайту" + " - " + current_time_in_site)
print("Час на комп'ютері" + " - " + str(current_time_in_laptop))
