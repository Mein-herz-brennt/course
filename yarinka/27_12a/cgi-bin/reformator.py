import cgi


def reformator(words: str):
    first = ""
    second = ""
    for i in words:
        if i.isdigit():
            first += i
        else:
            second += i
    return first, second


if __name__ == '__main__':
    form = cgi.FieldStorage()
    words = form.getfirst("string", "")
    strings = reformator(words)
    with open("result.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    html_content = html_content.replace("first", strings[0])
    html_content = html_content.replace("second", strings[1])
    print('Content-Type: text/html; charset=utf-8\n')
    print(html_content)
