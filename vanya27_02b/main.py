from wsgiref.simple_server import make_server
import cgi

HOST = ""
PORT = 9000


def odnakovi(wrd1: str, wrd2: str):
    wd1 = list(set(wrd1.split(" ")))
    wd2 = list(set(wrd2.split(" ")))
    words = wd1 + wd2
    words_set = list(set(wd1 + wd2))
    for i in words_set:
        words.remove(i)
    return " ".join(words)


def application(env, start_response):
    with open("index.html", "r", encoding="utf-8") as file:
        text = file.read()

    word = cgi.FieldStorage(fp=env["wsgi.input"], environ=env)
    word1 = word.getfirst("first", "")
    word2 = word.getfirst("second", "")

    if word1 != "" and word2 != "":
        result = odnakovi(str(word1), str(word2))
        with open("out_index.html", encoding="utf-8") as file:
            html_content = file.read()
        html_content = html_content.replace("res", result)
        start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes(html_content, encoding="utf-8")]
    else:
        # print(*env.items(), sep="\n")
        start_response("200 OK", [("Content-type:", "text/html;  cherset=utf-8")])
        return [bytes(text, encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{PORT}')
    httpd = make_server(HOST, PORT, application)
    httpd.serve_forever()
