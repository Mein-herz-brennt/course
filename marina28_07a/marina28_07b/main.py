from wsgiref.simple_server import make_server
import cgi
from driver import *

HOST = ""
port = 8777
OPTION = """<option value="cur">cur</option>"""


def web_app(env, start_response):
    form = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)
    path = env.get("PATH_INFO", "")
    if path == "/":
        with open("index.html", "r", encoding="utf-8") as file:
            text = file.read()
        pib = form.getfirst("name", "") + " " + form.getfirst("last_name", "") + " " + form.getfirst("surname", "")
        price = form.getfirst("price")
        load_capacity = form.getfirst("load_capacity")
        if pib != "  " and price != "" and load_capacity != "":
            callback = Driver().add_driver(pib, price, load_capacity)
            html_content = text.replace("driver", callback)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(html_content, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]

    elif path == "/addWaybill.html":
        params = {"currencies": ""}
        with open("addWaybill.html", "r", encoding="utf-8") as file:
            text = file.read()
        pib = form.getfirst("pib", "")
        date = form.getfirst("date", "")
        number = form.getfirst("distance", "")
        if pib != "" and date != "" and number != "":
            waybill = Driver().add_waybill(pib, date, number)
            currencies = ""
            for cur in Driver().get_currencies():
                currencies += OPTION.replace("cur", cur)
            params["currencies"] = currencies
            page = text.replace("currencies", params["currencies"])
            page = page.replace("add_waybill", waybill)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(page, encoding="utf-8")]
        else:
            currencies = ""
            for cur in Driver().get_currencies():
                currencies += OPTION.replace("cur", cur)
            params["currencies"] = currencies
            page = text.replace("currencies", params["currencies"])
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(page, encoding="utf-8")]
    elif path == "/check_pay.html":
        params = {"currencies": ""}
        with open("check_pay.html", "r", encoding="utf-8") as file:
            text = file.read()
        pib = form.getfirst("pib", "")
        date1 = form.getfirst("date1", "")
        date2 = form.getfirst("date2", "")
        if pib != "" and date1 != "" and date2 != "":
            pay = Driver().pay_for_km(pib, date1, date2)
            currencies = ""
            for cur in Driver().get_currencies():
                currencies += OPTION.replace("cur", cur)
            params["currencies"] = currencies
            page = text.replace("currencies", params["currencies"])
            page = page.replace("NAME", pib)
            page = page.replace("MONEY", str(pay))
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(page, encoding="utf-8")]
        else:
            currencies = ""
            for cur in Driver().get_currencies():
                currencies += OPTION.replace("cur", cur)
            params["currencies"] = currencies
            page = text.replace("currencies", params["currencies"])
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(page, encoding="utf-8")]
    else:
        start_response("404 Page not found", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes("Sorry but page not found 404", encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{port}')
    httpd = make_server(HOST, port, web_app)
    httpd.serve_forever()
