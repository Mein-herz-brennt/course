from wsgiref.simple_server import make_server
import cgi
import re

HOST = ""
port = 8000


def remover(string: str) -> str:
    res = re.sub(r'\([^)]*\)', '', string)
    return res


def web_application(env, start_response):
    with open("index.html", "r", encoding="utf-8") as file:
        text = file.read()

    form = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)

    string = form.getfirst("string", "")
    if string != "":
        with open("out.html", "r", encoding="utf-8") as file:
            text = file.read()
        text = text.replace("result", remover(string))
        start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes(text, encoding="utf-8")]
    else:
        # print(*env.items(), sep="\n")
        start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes(text, encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{port}')
    httpd = make_server(HOST, port, web_application)
    httpd.serve_forever()
