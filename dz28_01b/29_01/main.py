from wsgiref.simple_server import make_server
import cgi
from toy import *

HOST = ""
port = 8000
OPTION = """<option value="cur">cur</option>"""


def web_app(env, start_response):
    path = env.get("PATH_INFO", "")
    form = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)
    toys = Toy("TOYS.db")

    option = ""
    if path == "/":
        with open("index.html", "r", encoding="utf-8") as file:
            text = file.read()
        name = form.getfirst("name", "")
        if name == "":
            for i in toys.get_all_toys_names():
                option += OPTION.replace("cur", i)
            html_content = text.replace("currencies", option)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(html_content, encoding="utf-8")]

        elif name != "":
            for i in toys.get_all_toys_names():
                option += OPTION.replace("cur", i)
            html_content = text.replace("currencies", option)
            data = ""
            igraschi = toys.find_toy_by_name(name)
            for i in igraschi:
                data += i
            html_content = html_content.replace("result", data)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(html_content, encoding="utf-8")]

    elif path == "/add_new_toy.html":
        with open("add_new_toy.html", "r", encoding="utf-8") as file:
            text = file.read()
        name = form.getfirst("title", "")
        min_age = form.getfirst("min_age", "")
        max_age = form.getfirst("max_age", "")
        price = form.getfirst("price", "")
        if name != "" and min_age != "" and max_age != "" and price != "":
            res = toys.add_toy(name, min_age, max_age, int(price))
            text = text.replace("result", res)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]

    elif path == "/delete_toy.html":
        with open("delete_toy.html", "r", encoding="utf-8") as file:
            text = file.read()
            cur = ""
            for i in toys.get_all_toys_names():
                cur += OPTION.replace("cur", i)
            text = text.replace("currencies", cur)
        name = form.getfirst("name", "")
        if name != "":
            inf = toys.delete_toy(name)
            text = text.replace("result", inf)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]

    elif path == "/update_toy.html":
        with open("update_toy.html", "r", encoding="utf-8") as file:
            text = file.read()
        cur = ""
        for i in toys.get_all_toys_names():
            cur += OPTION.replace("cur", i)
        text = text.replace("currencies", cur)
        name = form.getfirst("name", "")
        min_age = form.getfirst("min_age", "")
        max_age = form.getfirst("max_age", "")
        price = form.getfirst("price", "")
        if name != "" and min_age != "" and max_age != "" and price != "":
            inf = toys.update_toy(name, min_age, max_age, price)
            text = text.replace("result", inf)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]

    elif path == "/find_by_age.html":
        age = form.getfirst("years", "")
        with open("find_by_age.html", "r", encoding="utf-8") as file:
            text = file.read()
        if age == "":
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        elif age != "":
            data = ""
            igraschi = toys.find_toys_by_years(years=int(age))
            for i in igraschi:
                data += i
            html_content = text.replace("result", data)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(html_content, encoding="utf-8")]

    elif path == "/find_by_price.html":
        with open("find_by_price.html", "r", encoding="utf-8") as file:
            text = file.read()
        price_min = form.getfirst("price_min", "")
        price_max = form.getfirst("price_max", "")

        data = ""
        if price_min == "" and price_max == "":
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        elif price_min != "" and price_max == "":
            html_content = text.replace("result", """Заповніть обидва поля з ціною """)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(html_content, encoding="utf-8")]
        elif price_max != "" and price_min == "":
            html_content = text.replace("result", """Заповніть обидва поля з ціною""")
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(html_content, encoding="utf-8")]
        elif price_min != "" and price_max != "":
            igraschi = toys.find_by_min_and_max_price(min_price=int(price_min), max_price=int(price_max))
            for i in igraschi:
                data += i
        html_content = text.replace("result", data)
        start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes(html_content, encoding="utf-8")]

    else:
        start_response("404 PAGE NOT FOUND", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes("Error 404", encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{port}')
    httpd = make_server(HOST, port, web_app)
    httpd.serve_forever()
