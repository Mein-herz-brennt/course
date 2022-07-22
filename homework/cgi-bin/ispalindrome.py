import cgi


def palindrome(word: str):
    if word == word[::-1]:
        return f"{word} is Palindrome"
    else:
        return f"{word} Not Palindrome"


if __name__ == '__main__':
    import os

    if os.name == "nt":
        import sys, codecs

        sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer)
    words = cgi.FieldStorage()
    words = words.getfirst("palindrom input")
    with open("out_index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    html_content = html_content.replace("HOHOHO", palindrome(words))
    print('Content-Type: text/html; charset=utf-8\n')
    print(html_content)
