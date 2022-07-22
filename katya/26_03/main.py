from html.parser import HTMLParser
import requests
import datetime

# https://www.meteoprog.ua/ua/weather/{city}/  (link for city) Посилання дає прогноз погоди лише на 4 дні
# На сьогодні та на 3 наступні


def generate_link(city: str):
    link = f"https://www.meteoprog.ua/ua/weather/{city}/"
    req = requests.get(link).text
    if "404" and "Сторінку не знайдено" in req:
        print(req)
        raise ValueError("Sorry, the city is entered incorrectly, try to enter the name of the city in English, "
                         "if this does not help, then there is no point for such a city on the site")
    return link


def get_html_code_from_site(link: str):
    req = requests.get(link).text
    return req


class WeatherHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.temp = False

    def handle_starttag(self, tag, attrs):
        if tag == "h6":
            self.temp = True

    def handle_data(self, data):
        if self.temp:
            print(data)

    def handle_endtag(self, tag):
        if tag == "h6":
            self.temp = False


def main(city: str):  # please enter the city name in English
    html = get_html_code_from_site(generate_link("Kyiv"))
    weather = WeatherHTMLParser()
    print(datetime.date.today())
    weather.feed(html)


if __name__ == '__main__':
    main(str(input("please enter the city name in English: ")))
