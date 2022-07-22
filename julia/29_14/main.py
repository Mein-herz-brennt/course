import xml.etree.ElementTree as et
import cgi
import sqlite3
from string import Template
import datetime

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()


OPTION = """<option>$name</option>"""
OPTION_1 = """<h5>$info_text</h5>"""


class EmployeesXML:
    def __init__(self, employees, report_cards, result_list):
        self.employees = employees
        self.report_cards = report_cards
        self.result_list = result_list

    def get_info_employees(self):
        etree = et.parse(self.employees)
        employees_el = etree.find("employees")
        employees = []
        for i in employees_el:
            employee = (
                i.text,
                int(i.get("salary_per_hour")),
                int(i.get("work_hours_per_day"))
            )
            employees.append(employee)
        return employees

    def get_report_cards(self):
        etree = et.parse(self.report_cards)
        report_cards_el = etree.find("report_cards")
        report_cards = []
        for i in report_cards_el:
            add = [i.get("name")]
            for j in i:
                day = (j.text,
                       int(j.get("hours")))
                add.append(day)
            report_cards.append(add)
        return report_cards

    def salary(self, employee):
        report_card = {}
        salary = 0
        for i in self.get_report_cards():
            if i[0] == employee[0]:
                report_card = i
        for j in report_card:
            if j == employee[0]:
                pass
            else:
                salary += (j[1] * employee[1])
        return salary

    def create_xml(self):
        result_list = []
        employees = self.get_info_employees()

        for i in employees:
            salary = self.salary(i)
            result_list.append([i[0], salary])
        root = et.Element("data")
        info_students = et.Element("employees")
        counter = 0
        for employee in result_list:
            attrib = {"salary": str(employee[1])}
            et.SubElement(info_students, "salary", attrib)
            info_students[counter].text = employee[0]
            counter += 1
        root.append(info_students)
        etree = et.ElementTree(root)
        etree.write(self.result_list, encoding="utf-8", xml_declaration=True)

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "").lstrip("/")
        params = {"employees": "", "info_text": ""}
        status = "200 OK"
        headers = [("Content-Type", "text/html; charset=utf-8")]
        file = "templates/employees.html"

        if path == "":
            self.create_xml()
            employees = ""
            etree = et.parse(self.result_list)
            employees_el = etree.find("employees")
            for i in employees_el:
                info_employee = i.text + " - " + i.get("salary") + " грн."
                employees += Template(OPTION).substitute(name=info_employee)
            params["employees"] = employees

        elif path == "data/employees.xml":
            headers = [("Content-Type", "text/xml; charset=utf-8")]
            file = "data/report_cards.xml"

        elif path == "templates/add_info_to_report_cards.html":
            headers = [("Content-Type", "text/html; charset=utf-8")]
            file = "templates/add_info_to_report_cards.html"
            employees = ""
            for i in self.get_info_employees():
                employees += Template(OPTION).substitute(name=i[0])
            params["employees"] = employees

        elif path == "report_cards.xml":
            form = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)
            name = form.getfirst("employee", "")
            date = form.getfirst("date", "")
            hours = form.getfirst("hours", "")
            info = ""
            now_month = datetime.datetime.now().month
            if name and date and hours:
                try:
                    etree = et.parse(self.report_cards)
                    report_cards_el = etree.find("report_cards")
                    for i in report_cards_el:
                        if name in i.get("name"):
                            new_date = date.split("-")
                            res_date = ".".join(new_date[::-1])
                            for j in i:
                                if res_date in j.text or int(res_date[3:5]) != (now_month - 1):
                                    raise ValueError
                                else:
                                    if 0 > int(hours) > 24:
                                        raise ValueError

                            attrib = {"hours": hours}
                            et.SubElement(i, "work", attrib)
                            i[-1].text = res_date
                    etree.write(self.report_cards, encoding="utf-8", xml_declaration=True)
                    info = "Інформація додана до табелю!"

                except ValueError:
                    info = "Інформація введена не вірно перевірте вхідні дані!!"
                text = ''
                text += Template(OPTION_1).substitute(info_text=info)
                params["info_text"] = text

                employees = ""
                for i in self.get_info_employees():
                    employees += Template(OPTION).substitute(name=i[0])
                params["employees"] = employees

                file = "templates/add_info_to_report_cards.html"
            else:
                status = "303 SEE OTHER"
                headers.append(("Location", "report_cards.xml"))

        else:
            status = "404 NOT FOUND"
            file = "templates/error_404.html"

        start_response(status, headers)
        with open(file, encoding="utf-8") as f:
            page = Template(f.read()).substitute(params)
        return [bytes(page, encoding="utf-8")]


if __name__ == "__main__":
    HOST = ""
    PORT = 8100
    app = EmployeesXML(
        "data/employees.xml",
        "data/report_cards.xml",
        "data/result_list.xml")

    httpd = make_server(HOST, PORT, app)
    print(" === Local webserver === ")
    print(f"http://localhost:{PORT}")
    httpd.serve_forever()
