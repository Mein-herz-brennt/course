from wsgiref.simple_server import make_server
import cgi

HOST = ""
port = 7000


def html_reader(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def get_parni(string: str):
    lst_str = string.split(" ")
    parni = []
    for i in range(len(lst_str)):
        if i % 2 == 0:
            parni.append(lst_str[i])
    return " ".join(parni)


def app(env, start_response):
    text = html_reader("index.html")

    form = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)

    words = form.getfirst("words", "")
    if words:
        start_response("200 OK", [("Content-Type:", "text/html;  cherset=utf-8")])
        html_content = text.replace("result", get_parni(words))
        return [bytes(html_content, encoding="utf-8")]
    else:
        start_response("200 OK", [("Content-Type:", "text/html;  cherset=utf-8")])
        html_content = text.replace("result", "")
        return [bytes(html_content, encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{port}')
    httpd = make_server(HOST, port, app)
    httpd.serve_forever()
