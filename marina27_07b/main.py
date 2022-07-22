from wsgiref.simple_server import make_server
import cgi

HOST = ""
port = 777


def dot(vector1: list, vector2: list):
    if len(vector1) != len(vector2):
        return "Ви вказали вектори різної розмірності"
    try:
        for i in range(len(vector1)):
            vector1[i] = float(vector1[i])
        for i in range(len(vector2)):
            vector2[i] = float(vector2[i])
        dot = sum(p * q for p, q in zip(vector1, vector2))
        return str(dot)
    except Exception:
        return "Елементи вектора повинні бути числами записаними через пробіл"


def web_app(env, start_response):
    with open("index.html", "r", encoding="utf-8") as file:
        text = file.read()

    form = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)
    vector1 = form.getfirst("first", "")
    vector2 = form.getfirst("second", "")

    if vector1 != "" and vector2 != "":
        result = dot(str(vector1).split(" "), str(vector2).split(" "))
        with open("out_index.html", encoding="utf-8") as file:
            html_content = file.read()
        html_content = html_content.replace("res1", vector1)
        html_content = html_content.replace("res2", vector2)
        html_content = html_content.replace("res3", result)
        start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes(html_content, encoding="utf-8")]
    else:
        # print(*env.items(), sep="\n")
        start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes(text, encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{port}')
    httpd = make_server(HOST, port, web_app)
    httpd.serve_forever()
