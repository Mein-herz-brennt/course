from bs4 import BeautifulSoup
import requests

req = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2")

soup = BeautifulSoup(req.text, "lxml")
day = soup.find("p", class_="day-link").text
day_num = soup.find("p", class_="date").text
month = soup.find("p", class_="month").text
temps = soup.find("tr", class_="temperature").find_all("td")
all_temps = []
for temp in temps:
    all_temps.append(temp.text[:-1])

for i in range(len(all_temps)):
    all_temps[i] = int(all_temps[i])

print(day + " - " + day_num + " " + month + " - " + f"max_temp: {max(all_temps)}, min_temp: {min(all_temps)}")
print("all temps in these day: ")

for i in all_temps:
    print(i)
