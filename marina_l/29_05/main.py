from wsgiref.simple_server import make_server
import cgi
from Hotel import *

HOST = ""
port = 7000
OPTION = """<option value="cur">cur</option>"""


def read_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def web_app(env, start_response):
    room_head = Room()
    user = User()
    form = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)
    path = env.get("PATH_INFO", "")
    if path == "/":
        text = read_file("index.html")
        room_type = form.getfirst("type", "")
        pay_day = form.getfirst("pay_for_day", "")
        room = form.getfirst("room1", "")
        if room != "" and room_type != "" and pay_day != "":
            res = room_head.add_room(room_type, room, pay_day)
            html_content = text.replace("result", res)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(html_content, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]

    elif path == "/second.html":
        text = read_file("second.html")
        room = form.getfirst("room", "")
        pib = form.getfirst("pib", "")
        date = form.getfirst("days", "")
        if room != "" and pib != "" and date != "":
            opt = ""
            for i in room_head.get_currency():
                opt += OPTION.replace("cur", str(i))
            text = text.replace("currencies", opt)
            res = user.add_user(pib, room, date)
            html_content = text.replace("result", res)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(html_content, encoding="utf-8")]
        else:
            opt = ""
            for i in room_head.get_currency():
                opt += OPTION.replace("cur", str(i))
            text = text.replace("currencies", opt)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
    elif path == "/delete.html":
        with open("delete.html", "r", encoding="utf-8") as file:
            text = file.read()
        cur = ''
        for i in Room().get_currency():
            cur += OPTION.replace("cur", str(i))
        text = text.replace("currencies", cur)
        name = form.getfirst("name", "")
        if name != "":
            text = text.replace("result", User().delete_room(int(name)))
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]

    elif path == "/update.html":
        with open("update.html", "r", encoding="utf-8") as file:
            text = file.read()
        cur1 = ""
        cur2 = ""
        for i in Room().get_currency():
            cur1 += OPTION.replace("cur", str(i))
        for i in User().get_cur():
            cur2 += OPTION.replace("cur", i)
        text = text.replace("currencies1", cur1)
        text = text.replace("currencies2", cur2)
        room = form.getfirst("room", "")
        name = form.getfirst("name", "")
        days = form.getfirst("days", "")
        if room != "" and name != "" and days != "":
            text = text.replace("result", User().update_info_about_user(name, int(room), int(days)))
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
    elif path == "/third.html":
        text = read_file("third.html")
        check = form.getfirst("check", "")
        room = form.getfirst("room3", "")
        if check == "Розрахувати всіх" and room != "":
            opt = ""
            for i in room_head.get_currency():
                opt += OPTION.replace("cur", str(i))
            text = text.replace("currencies", opt)
            res = user.pay_for_all()
            html_content = text.replace("result", res)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(html_content, encoding="utf-8")]

        elif check == "Розрахувати одного" and room != "":
            opt = ""
            for i in room_head.get_currency():
                opt += OPTION.replace("cur", str(i))
            text = text.replace("currencies", opt)
            res = user.pay_for_one(room)
            html_content = text.replace("result", res)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(html_content, encoding="utf-8")]
        else:
            opt = ""
            for i in room_head.get_currency():
                opt += OPTION.replace("cur", str(i))
            text = text.replace("currencies", opt)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
    else:
        start_response("404 PAGE NOT FOUND", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes("Error 404 PAGE NOT FOUND", encoding="utf-8")]

if __name__ == '__main__':
    print(f'Starting server in http://localhost:{port}')
    httpd = make_server(HOST, port, web_app)
    httpd.serve_forever()
