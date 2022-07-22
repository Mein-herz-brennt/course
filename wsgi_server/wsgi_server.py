from wsgiref.simple_server import make_server
import cgi

HOST = ""
port = 800


def dict_str(string: str):
    k = {}
    string = string.split(' ')
    print(string)
    for i in string:
        counter = 0
        print("i ->", i)
        for j in string:
            print("j ->", j)
            if i == j:
                counter += 1
                k[i] = counter
                print("counter ->", counter)
    return str(k)


def app(env, start_response):
    with open("index.html", "r", encoding="utf-8") as file:
        text = file.read()

    words = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)

    words = words.getfirst("palindrom input", "")
    if words != "":
        with open("out_index.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        html_content = html_content.replace("HOHOHO", dict_str(words))
        start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes(html_content, encoding="utf-8")]
    else:
        # print(*env.items(), sep="\n")
        start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes(text, encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{port}')
    httpd = make_server(HOST, port, app)
    httpd.serve_forever()
