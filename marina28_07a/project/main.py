from wsgiref.simple_server import make_server
import cgi
from work_with_files import *

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
        file = "add_new_emp.html"
        cur = ""
        for i in _work_with_db.get_all_departments_names():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("curr", cur)
        cur1 = ""
        for i in _work_with_db.get_all_position_names():
            cur1 += OPTION.replace("cur", i)
        page = page.replace("cur", cur1)
        name = form.getfirst("pib", "")
        department = form.getfirst("department", "")
        position = form.getfirst("position", "")
        salary_per_hour = form.getfirst("salary_per_hour", "")
        hours_in_day = form.getfirst("hours_in_day", "")
        if name and department and position and salary_per_hour and hours_in_day:
            name_ = "_".join(name.split(" "))
            _work_with_db.add_employee(name_, department, position, salary_per_hour, hours_in_day)
            file_xml = _work_with_db.get_info_about_file("Прийняття робітника", name_)
            files.append(file_xml[2])
            cur = OPTION1.replace("cur", file_xml[2])
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "add_new_car.html":
        file = "add_new_dep.html"
        cur = ""
        name = form.getfirst("name", "")
        department = form.getfirst("caption", "")
        if name and department:
            emp = _work_with_db.get_all_employees_names_by_dep(name)
            cur = _work_with_db.add_department(name, department, emp, len(emp))
            page = html_reader(file).replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = html_reader(file).replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "bye_detail.html":
        file = "add_new_pos.html"
        cur = ""
        for i in _work_with_db.get_all_departments_names():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("cur", cur)
        name = form.getfirst("name", "")
        caption = form.getfirst("caption", "")
        department = form.getfirst("department", "")
        if name and caption and department:
            emp = _work_with_db.get_all_employees_names_by_dep(name)
            cur = _work_with_db.add_position(name, caption, emp, len(emp), department)
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "update_car.html":
        file = "update_emp.html"
        cur = ""
        cur0 = ""
        for i in _work_with_db.get_all_employees_names():
            cur0 += OPTION.replace("cur", i)
        page = html_reader(file).replace("currr", cur0)
        for i in _work_with_db.get_all_departments_names():
            cur += OPTION.replace("cur", i)
        page = page.replace("curr", cur)
        cur1 = ""
        for i in _work_with_db.get_all_position_names():
            cur1 += OPTION.replace("cur", i)
        page = page.replace("cur", cur1)
        name = form.getfirst("pib", "")
        department = form.getfirst("department", "")
        position = form.getfirst("position", "")
        salary_per_hour = form.getfirst("salary_per_hour", "")
        hours_in_day = form.getfirst("hours_in_day", "")
        if name and department and position and salary_per_hour and hours_in_day:
            name_ = "_".join(name.split(" "))
            _work_with_db.update_employee(name_, department, position, salary_per_hour, hours_in_day)
            file_xml = _work_with_db.get_info_about_file("Переведення на посаду", name_)
            files.append(file_xml[2])
            cur = OPTION1.replace("cur", file_xml[2])
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "update_det.html":
        file = "update_dep.html"
        cur = ""
        for i in _work_with_db.get_all_departments_names():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("cur", cur)
        name = form.getfirst("name", "")
        department = form.getfirst("caption", "")
        if name and department:
            emp = _work_with_db.get_all_employees_names_by_dep(name)
            cur = _work_with_db.update_department(name, department, emp, len(emp))
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "update_pos.html":
        file = "update_pos.html"
        cur = ""
        cur0 = ""
        for i in _work_with_db.get_all_departments_names():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("curr", cur)
        for i in _work_with_db.get_all_position_names():
            cur0 += OPTION.replace("cur", i)
        page = page.replace("cur", cur0)
        name = form.getfirst("name", "")
        caption = form.getfirst("caption", "")
        department = form.getfirst("department", "")
        if name and caption and department:
            emp = _work_with_db.get_all_employees_names_by_dep(name)
            cur = _work_with_db.update_position(name, caption, emp, len(emp), department)
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "delete_det.html":
        file = "delete_emp.html"
        cur = ""
        for i in _work_with_db.get_all_employees_names():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("curr", cur)
        name = form.getfirst("pib", "")
        if name:
            name_ = "_".join(name.split(" "))
            _work_with_db.delete_employee(name_)
            file_xml = _work_with_db.get_info_about_file("Звільнення", name_)
            files.append(file_xml[2])
            cur = OPTION1.replace("cur", file_xml[2])
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "delete_pos.html":
        file = "delete_pos.html"
        cur0 = ""
        cur = ""
        for i in _work_with_db.get_all_departments_names():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("curr", cur)
        for i in _work_with_db.get_all_position_names():
            cur0 += OPTION.replace("cur", i)
        page = page.replace("cur", cur0)
        name = form.getfirst("name", "")
        department = form.getfirst("department", "")
        if name and department:
            cur = _work_with_db.delete_position(name, department)
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "delete_car.html":
        file = "delete_dep.html"
        for i in _work_with_db.get_all_departments_names():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("cur", cur)
        name = form.getfirst("name", "")
        if name:
            cur = _work_with_db.delete_department(name)
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "add_report_card.html":
        file = "add_report_card.html"
        cur = ""
        for i in _work_with_db.get_all_employees_names():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("cur", cur)
        name = form.getfirst("name", "")
        date = form.getfirst("date", "")
        hours = form.getfirst("hours", "")
        dep = form.getfirst("department", "")
        pos = form.getfirst("position", "")
        if name and date and hours and dep and pos:
            cur = _work_with_db.add_report_card(name, dep, pos, date, hours)
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "add_result_card.html":
        file = "add_result_card.html"
        cur = ""
        for i in _work_with_db.get_all_employees_names():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("cur", cur)
        name = form.getfirst("name", "")
        dep = form.getfirst("department", "")
        pos = form.getfirst("position", "")
        if name and dep and pos:
            cur = _work_with_db.add_result_card(name, dep, pos)
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "update_report_card.html":
        file = "update_report_card.html"
        cur = ""
        for i in _work_with_db.get_all_employees_names():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("cur", cur)
        name = form.getfirst("name", "")
        date = form.getfirst("date", "")
        hours = form.getfirst("hours", "")
        dep = form.getfirst("department", "")
        pos = form.getfirst("position", "")
        if name and date and hours and dep and pos:
            cur = _work_with_db.update_report_card(name, dep, pos, date, hours)
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path == "update_result_card.html":
        file = "update_result_card.html"
        cur = ""
        for i in _work_with_db.get_all_employees_names():
            cur += OPTION.replace("cur", i)
        page = html_reader(file).replace("cur", cur)
        name = form.getfirst("name", "")
        dep = form.getfirst("department", "")
        pos = form.getfirst("position", "")
        if name and dep and pos:
            cur = _work_with_db.update_result_card(name, dep, pos)
            page = page.replace("result", cur)
            start_response(status, headers)
            return [bytes(page, encoding="utf-8")]
        else:
            start_response(status, headers)
            page = page.replace("result", "")
            return [bytes(page, encoding="utf-8")]

    elif path in files:
        file = path
        status = "303 SEE OTHER"
        headers = [("Content-Type", "text/xml; charset=utf-8")]
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
