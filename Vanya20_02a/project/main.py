from wsgiref.simple_server import make_server
import cgi
from work_with_db import *

HOST = ""
PORT = 9000
OPTION = """<option value="cur">cur</option>"""
OPTION1 = """<a href="/cur" target="_blank">Наказ</a>"""


def html_reader(filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        page = f.read()
    return page


files = []
cur = ""


def web_application(environ, start_response):
    global files, cur
    headers = [("Content-Type", "text/html; charset=utf-8")]
    status = "200 OK"
    file = "index.html"
    path = environ.get("PATH_INFO", "").lstrip("/")
    form = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)
    _work_with_db = WorkWithDB()
    if path == "":
        file = "index.html"
        page = html_reader(file)
        start_response(status, headers)
        return [bytes(page, encoding="utf-8")]
    elif path == "add_new_det.html":
        file = "add_new_det.html"
        cur = ""
        for i in _work_with_db.get_all_car_marks():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("curr", cur)
        cur1 = ""
        for i in _work_with_db.get_all_car_models():
            cur1 += OPTION.replace("cur", i)
        page = page.replace("cur", cur1)
        name = form.getfirst("pib", "")
        mark = form.getfirst("mark", "")
        model = form.getfirst("model", "")
        category = form.getfirst("category", "")
        pay = form.getfirst("pay", "")
        date = form.getfirst("date", "")
        if name and mark and model and pay and date and category:
            res = _work_with_db.add_detail(name, mark, model, category, date, pay)
            page = page.replace("result", res)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "add_new_car.html":
        file = "add_new_car.html"
        cur = ""
        name = form.getfirst("name", "")
        capt = form.getfirst("caption", "")
        date = form.getfirst("date", "")
        if name and capt and date:
            cur = _work_with_db.add_car(name, capt, date)
            page = html_reader(file).replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = html_reader(file).replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "update_det.html":
        file = "update_det.html"
        cur = ""
        cur0 = ""
        for i in _work_with_db.get_all_details_names():
            cur0 += OPTION.replace("cur", i)
        page = html_reader(file).replace("currr", cur0)
        for i in _work_with_db.get_all_car_marks():
            cur += OPTION.replace("cur", i)
        page = page.replace("curr", cur)
        cur1 = ""
        for i in _work_with_db.get_all_car_models():
            cur1 += OPTION.replace("cur", i)
        page = page.replace("cur", cur1)
        name = form.getfirst("name", "")
        mark = form.getfirst("mark", "")
        model = form.getfirst("model", "")
        category = form.getfirst("category", "")
        pay = form.getfirst("pay", "")
        date = form.getfirst("date", "")
        if name and mark and model and pay and date and category:
            cur = _work_with_db.update_detail(name, mark, model, category, date, pay)
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "update_car.html":
        file = "update_car.html"
        cur = ""
        for i in _work_with_db.get_all_car_marks():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("curr", cur)
        cur0 = ""
        for i in _work_with_db.get_all_car_models():
            cur0 += OPTION.replace("cur", i)
        page = page.replace("cur", cur0)
        mark = form.getfirst("mark", "")
        model = form.getfirst("model", "")
        date = form.getfirst("date", "")
        if mark and model and date:
            cur = _work_with_db.update_car(mark, model, date)
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "delete_det.html":
        file = "delete_det.html"
        cur = ""
        cur0 = ""
        for i in _work_with_db.get_all_details_names():
            cur0 += OPTION.replace("cur", i)
        page = html_reader(file).replace("currr", cur0)
        for i in _work_with_db.get_all_car_marks():
            cur += OPTION.replace("cur", i)
        page = page.replace("curr", cur)
        cur1 = ""
        for i in _work_with_db.get_all_car_models():
            cur1 += OPTION.replace("cur", i)
        page = page.replace("cur", cur1)
        name = form.getfirst("name", "")
        mark = form.getfirst("mark", "")
        model = form.getfirst("model", "")
        date = form.getfirst("date", "")
        if name and mark and model and date:
            cur = _work_with_db.delete_detail(name, model, mark, date)
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "delete_car.html":
        file = "delete_car.html"
        cur0 = ""
        cur = ""
        for i in _work_with_db.get_all_car_marks():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("curr", cur)
        for i in _work_with_db.get_all_car_models():
            cur0 += OPTION.replace("cur", i)
        page = page.replace("cur", cur0)
        mark = form.getfirst("mark", "")
        model = form.getfirst("model", "")
        date = form.getfirst("date", "")
        if mark and model and date:
            cur = _work_with_db.delete_car(model, mark, date)
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "bye_detail.html":
        file = "bye_detail.html"
        cur = ""
        name = form.getfirst("name", "")
        category = form.getfirst("category", "")
        if name:
            filename = _work_with_db.get_info_about_details_by_name(name)[1]
            files.append(filename)
            cur = OPTION1.replace("cur", filename)
            page = html_reader(file).replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        elif category:
            filename = _work_with_db.get_info_about_details_by_category(category)[1]
            files.append(filename)
            cur = OPTION1.replace("cur", filename)
            page = html_reader(file).replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = html_reader(file).replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path in files:
        file = path
        status = "303 SEE OTHER"
        headers = [("Content-Type", "text/json; charset=utf-8")]
        page = html_reader(file)
        start_response(status, headers)
        return [bytes(page, encoding="utf-8")]
    else:
        status = "404 NOT FOUND"
        file = "error_404_page.html"
        start_response(status, headers)
        page = html_reader(file)
        return [bytes(page, encoding="utf-8")]


if __name__ == '__main__':
    print(f'Starting server in http://localhost:{PORT}')
    httpd = make_server(HOST, PORT, web_application)
    httpd.serve_forever()
