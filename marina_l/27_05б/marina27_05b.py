from wsgiref.simple_server import make_server
import cgi

HOST = ""
port = 7000


def maxmin(list_max_min: str):
    list_max_min = list_max_min.split(" ")
    for i in range(len(list_max_min)):
        try:
            list_max_min[i] = float(list_max_min[i])
        except Exception as e:
            return e
    list_vidp = [str(max(list_max_min)), str(min(list_max_min))]
    return list_vidp


def web_app(env, start_response):
    with open("index.html", "r", encoding="utf-8") as file:
        text = file.read()

    list_nums = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)
    list_num = list_nums.getfirst("maxmin input", "")
    if list_num != "":
        with open("out_index.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        max_min = maxmin(list_num)
        if type(max_min) == list:
            html_content = html_content.replace("maxmin", list_num)
            html_content = html_content.replace("maximum", max_min[0])
            html_content = html_content.replace("minimum", max_min[1])
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(html_content, encoding="utf-8")]
        else:
            html_content = html_content.replace("maxmin", str(max_min))
            start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
            return [bytes(html_content, encoding="utf-8")]
    else:
        start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes(text, encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{port}')
    httpd = make_server(HOST, port, web_app)
    httpd.serve_forever()
