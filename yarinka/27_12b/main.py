from wsgiref.simple_server import make_server
import cgi

HOST = ""
port = 7000


def reformator(words: str):
    first = ""
    second = ""
    for i in words:
        if i.isdigit():
            first += i
        else:
            second += i
    return first, second


def web_app(env, start_response):
    form = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)
    words = form.getfirst("string", "")
    if words:
        with open("result.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        strings = reformator(words)
        html_content = html_content.replace("first", strings[0])
        html_content = html_content.replace("second", strings[1])
        start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes(html_content, encoding="utf-8")]
    else:
        with open("index.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes(html_content, encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{port}')
    httpd = make_server(HOST, port, web_app)
    httpd.serve_forever()
