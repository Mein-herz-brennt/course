from wsgiref.simple_server import make_server
import cgi
from telephone_checker import *

HOST = ""
port = 9000


def web_app(env, start_response):
    form = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)
    path = env.get("PATH_INFO", "")
    if path == "/":
        with open("index.html", "r", encoding="utf-8") as file:
            text = file.read()
        name = form.getfirst("name", "")
        phone = form.getfirst("last_name", "")
        if name != "" and phone != "":
            html_content = FriendPhones().new_friend(name, phone)
            text = text.replace("Ну давай додай вже його!", html_content)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
    elif path == "/correct_name.html":
        with open("correct_name.html", "r", encoding="utf-8") as file:
            text = file.read()
        new_name = form.getfirst("name1", "")
        phone = form.getfirst("phone1", "")
        if new_name != "" and phone != "":
            html_content = FriendPhones().change_friend_name(new_name, phone)
            text = text.replace("Виправимо!", html_content)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
    elif path == "/correct_numb.html":
        with open("correct_numb.html", "r", encoding="utf-8") as file:
            text = file.read()
        name = form.getfirst("name2", "")
        new_phone = form.getfirst("phone2", "")
        if name != "" and new_phone != "":
            html_content = FriendPhones().change_friend_phone(name, new_phone)
            text = text.replace("Виправимо!", html_content)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
    elif path == "/find_person.html":
        with open("find_person.html", "r", encoding="utf-8") as file:
            text = file.read()
        name = form.getfirst("name3", "")
        phone = form.getfirst("phone3", "")
        if name != "" and phone == "":
            html_content = FriendPhones().find_friend(name, phone)
            text = text.replace("Попався негідник!", html_content)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        elif phone != "" and name == "":
            html_content = FriendPhones().find_friend(name, phone)
            text = text.replace("Попався негідник!", html_content)
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
        else:
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(text, encoding="utf-8")]
    else:
        start_response("404 Page not found", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes("Sorry but page not found 404", encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{port}')
    httpd = make_server(HOST, port, web_app)
    httpd.serve_forever()
