import cgi
import re


def remover(string: str) -> str:
    res = re.sub(r'\([^)]*\)', '', string)
    return res


if __name__ == '__main__':
    form = cgi.FieldStorage()
    string = form.getfirst("string")
    with open("out.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    html_content = html_content.replace("result", remover(string))
    print('Content-Type: text/html; charset=utf-8\n')
    print(html_content)
