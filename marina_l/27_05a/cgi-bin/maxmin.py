import cgi


def maxmin(list_max_min: str):
    list_max_min = list_max_min.split(" ")
    for i in range(len(list_max_min)):
        try:
            list_max_min[i] = float(list_max_min[i])
        except Exception as e:
            return e
    list_vidp = [str(max(list_max_min)), str(min(list_max_min))]
    return list_vidp


if __name__ == '__main__':
    list_nums = cgi.FieldStorage()
    list_num = list_nums.getfirst("maxmin input", "")
    max_min = maxmin(list_num)
    with open("out_index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    html_content = html_content.replace("maxmin", list_num)
    html_content = html_content.replace("maximum", max_min[0])
    html_content = html_content.replace("minimum", max_min[1])
    print('Content-Type: text/html; charset=utf-8\n')
    print(html_content)
