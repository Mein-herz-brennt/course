from bs4 import BeautifulSoup
import requests


def get_prognoz(city: str):
    if len(city.split(" ")) == 1:
        linc = f"https://ua.sinoptik.ua/погода-{city}"
    else:
        city = "-".join(city.split(" "))
        linc = f"https://ua.sinoptik.ua/погода-{city}"
    req = requests.get(linc)

    soup = BeautifulSoup(req.text, "lxml")
    day = soup.find("p", class_="day-link").text
    date = soup.find("p", class_="date").text
    month = soup.find("p", class_="month").text
    min_temp = soup.find("div", class_="temperature").find("div", class_="min").text
    max_temp = soup.find("div", class_="temperature").find("div", class_="max").text
    temp_in_this_moment = soup.find("p", class_="today-temp").text
    prognoz_for_day = soup.find("div", class_="wDescription clearfix").find("div", class_="description").text
    people_prognoz = soup.find("div", class_="oDescription clearfix").find("div", class_="description").text
    dict_of_prognoz = {"День": day,
                       "Дата": date,
                       "Місяць": month,
                       "Мінімальна температура": min_temp,
                       "Максимальна темперетура": max_temp,
                       "Температура зараз": temp_in_this_moment,
                       "Прогноз на день": prognoz_for_day,
                       "Народний прогноз": people_prognoz}
    return dict_of_prognoz


print(get_prognoz("Ковель"))
