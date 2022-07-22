from html.parser import HTMLParser
import requests


def generate_link(city: str):
    link = f"https://www.timeanddate.com/weather/ukraine/{city}/"
    req = requests.get(link).text
    if "404" and "Сторінку не знайдено" in req:
        print(req)
        raise ValueError("Sorry, the city is entered incorrectly, try to enter the name of the city in English, "
                         "if this does not help, then there is no point for such a city on the site")
    return link


def get_html_code_from_site(link: str):
    req = requests.get(link).text
    return req


class GetWeather(HTMLParser):
    def __init__(self):
        super().__init__()
        self.temp = False

    def handle_starttag(self, tag, attrs):
        if tag == "td" and ("class", "wa") in attrs:
            self.temp = True

    def handle_data(self, data):
        if self.temp:
            print(data)

    def handle_endtag(self, tag):
        if tag == "td":
            self.temp = False


def main():  # please enter the city name in English
    html = get_html_code_from_site(generate_link("Kyiv"))
    weather = GetWeather()
    weather.feed(html)


if __name__ == '__main__':
    main()