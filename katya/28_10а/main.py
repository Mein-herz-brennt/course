from wsgiref.simple_server import make_server
import cgi
from more_then_pay import *
import json

HOST = ""
port = 8000
OPTION = """<option value="cur">cur</option>"""


def web_app(env, start_response):
    path = env.get("PATH_INFO", "")
    form = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)
    cls = MoreThanPay("clients.xml", "products.xml", "number.xml", "payed.xml")
    if path == "/":
        with open("index.html", "r", encoding="utf-8") as file:
            text = file.read()
        cur = ""
        for i in cls.get_currencies():
            cur += OPTION.replace("cur", i)
        text = text.replace("currencies", cur)
        name = form.getfirst("name", "")
        if name != "":
            a = cls.result(name)
            with open(a, "r", encoding="utf-8") as file:
                res = file.read()
            start_response("303 SEE OTHER", [("Content-Type", "text/xml; charset=utf-8")])
            return [bytes(res, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-Type:", "text/html;  charset=utf-8")])
            return [bytes(text, encoding="utf-8")]

    elif path == "/adder.html":
        with open("adder.html", "r", encoding="utf-8") as file:
            text = file.read()
        name = form.getfirst("name", "")
        client_id = form.getfirst("client_id", "")
        address = form.getfirst("address", "")
        product = form.getfirst("product", "")
        product_id = form.getfirst("product_id", "")
        unit = form.getfirst("unit", "")
        price = form.getfirst("price", "")
        l_id = form.getfirst("l_id", "")
        no = form.getfirst("no", "")
        if name and client_id and address and product and product_id and unit and price and l_id and no:
            cls.add_new_client(name, address, client_id)
            cls.add_product(product_id, product, unit, price)
            cls.add_number(l_id, no, client_id)
            res = cls.add_payed(l_id, product_id, unit)
            text = text.replace("result", res)
            start_response("200 OK", [("Content-Type:", "text/html;  charset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-Type:", "text/html;  charset=utf-8")])
            return [bytes(text, encoding="utf-8")]
    else:
        start_response("404 ERROR", [("Content-Type:", "text/html;  charset=utf-8")])
        return [bytes("404 ERROR PAGE NOT FOUND", encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{port}')
    httpd = make_server(HOST, port, web_app)
    httpd.serve_forever()
