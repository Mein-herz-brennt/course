import sqlite3
import cgi
from string import Template
from wsgiref.simple_server import make_server
import datetime

OPTION = """<option>$name</option>"""
OPTION_1 = """<h5>$info_text</h5>"""


# Створення бази данних
#
# conn = sqlite3.connect("employees.db")
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE employees
#                   (name text, salary_per_hour int, work_hours_per_day int)
#                """)
# cursor.execute("""CREATE TABLE result_list
#                   (name text, salary int)
#                """)
# cursor.execute("""CREATE TABLE report_cards
#                   (name text, date text, hours int)
#                """)

class EmployeesDB:
    def __init__(self):
        self.conn = sqlite3.connect("employees.db")
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

    def get_info_employees(self):
        employees = self.cursor.execute("SELECT * FROM employees").fetchall()
        list_of = []
        for employee in employees:
            list_of.append({"name": employee[0],
                            "salary_per_hour": int(employee[1]),
                            "work_hours_per_day": int(employee[2])
                            }, )
        return list_of

    def get_report_cards(self):
        cards = self.cursor.execute("SELECT * FROM report_cards").fetchall()
        list_of = []
        for card in cards:
            crd = {"name": card[0]}
            for i in cards:
                if crd["name"] == i[0]:
                    crd[i[1]] = int(i[2])
                list_of.append(crd)
        return list_of

    def salary(self, employee):
        report_card = {}
        salary = 0
        for i in self.get_report_cards():
            if i["name"] == employee["name"]:
                report_card = i
        for j in report_card:
            if j == "name":
                pass
            else:
                salary += (report_card[j] * employee["salary_per_hour"])
        return salary

    def create_json(self):
        employees = self.get_info_employees()
        inf = []
        for i in employees:
            salary = self.salary(i)
            inf.append((i["name"], salary))
        self.cursor.executemany(f"""INSERT INTO result_list VALUES (?,?)""", inf)
        self.conn.commit()

    def get_names(self):
        names = self.cursor.execute("SELECT name FROM employees").fetchall()
        return names

    def get_dates(self, name):
        dates = self.cursor.execute(f"SELECT date FROM report_cards WHERE name = ?", (name))
        return dates

    def add_report_card(self, name, date, hours):
        inf = (name, date, hours)
        self.cursor.execute(f"""INSERT INTO report_cards VALUES (?,?,?)""", inf)
        self.conn.commit()
        return "Успішно додано!"

    def update_report_card(self, name, date, new_hours):
        sql = f"""
                UPDATE report_cards 
                SET hours = ?
                WHERE name = ? and date = ?
                """
        inf = (name, date, new_hours)
        self.cursor.execute(sql, inf)
        self.conn.commit()
        return "Успішно поновлено!"

    def delete_report_card(self, name, date):
        sql = f"""
                DELETE FROM report_cards
                WHERE name = ? and date = ?"""
        inf = (name, date)
        self.cursor.execute(sql, inf)
        self.conn.commit()
        return "Успішно видалено!"

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "").lstrip("/")
        params = {"employees": "", "info_text": ""}
        status = "200 OK"
        headers = [("Content-Type", "text/html; charset=utf-8")]
        file = "employees.html"

        if path == "":
            self.create_json()
            employees = ""
            lst = self.cursor.execute("SELECT * FROM result_list")
            for i in lst:
                info_employee = i[0] + " - " + str(i[1]) + " грн."
                employees += Template(OPTION).substitute(name=info_employee)
            params["employees"] = employees

        elif path == "reports.html":
            headers = [("Content-Type", "text/html; charset=utf-8")]
            file = "reports.html"
            params["employees"] = str(self.get_report_cards())

        elif path == "add_info_to_report_cards.html":
            headers = [("Content-Type", "text/html; charset=utf-8")]
            file = "add_info_to_report_cards.html"
            employees = ""
            for dct_1 in self.get_info_employees():
                employees += Template(OPTION).substitute(name=dct_1["name"])
            params["employees"] = employees

        elif path == "delete.html":
            headers = [("Content-Type", "text/html; charset=utf-8")]
            file = "delete.html"
            employees = ""
            for dct_1 in self.get_info_employees():
                employees += Template(OPTION).substitute(name=dct_1["name"])
            params["employees"] = employees

        elif path == "update.html":
            headers = [("Content-Type", "text/html; charset=utf-8")]
            file = "update.html"
            employees = ""
            for dct_1 in self.get_info_employees():
                employees += Template(OPTION).substitute(name=dct_1["name"])
            params["employees"] = employees

        elif path == "update_reports.html":
            form = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)
            name = form.getfirst("employee", "")
            date = form.getfirst("date", "")
            params["info_text"] = self.delete_report_card(name, date)
            headers = [("Content-Type", "text/html; charset=utf-8")]
            file = "delete.html"

        elif path == "delete_reports.html":
            form = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)
            name = form.getfirst("employee", "")
            date = form.getfirst("date", "")
            hours = form.getfirst("hours", "")
            params["info_text"] = self.update_report_card(name, date, hours)
            headers = [("Content-Type", "text/html; charset=utf-8")]
            file = "delete.html"

        elif path == "report_cards.json":
            form = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)
            name = form.getfirst("employee", "")
            date = form.getfirst("date", "")
            hours = form.getfirst("hours", "")
            info = ""
            now_month = datetime.datetime.now().month
            if name and date and hours:
                try:
                    if name in self.get_names():
                        res_date = date.split("-")
                        if res_date in self.get_dates(name) or int(res_date[3:5]) != (now_month - 1):
                            raise ValueError
                        else:
                            if 0 > int(hours) > 24:
                                raise ValueError
                            else:
                                info = self.add_report_card(name, res_date, hours)
                except ValueError:
                    info = "Інформація введена не вірно перевірте вхідні дані!!"
                text = ''
                text += Template(OPTION_1).substitute(info_text=info)
                params["info_text"] = text

                employees = ""
                for dct_1 in self.get_info_employees():
                    employees += Template(OPTION).substitute(name=dct_1["name"])
                params["employees"] = employees

                file = "add_info_to_report_cards.html"
            else:
                status = "303 SEE OTHER"
                headers.append(("Location", "teams.json"))

        else:
            status = "404 NOT FOUND"
            file = "error_404.html"

        start_response(status, headers)
        with open(file, encoding="utf-8") as f:
            page = Template(f.read()).substitute(params)
        return [bytes(page, encoding="utf-8")]


if __name__ == "__main__":
    HOST = ""
    PORT = 8100
    app = EmployeesDB()

    httpd = make_server(HOST, PORT, app)
    print(" === Local webserver === ")
    print(f"http://localhost:{PORT}")
    httpd.serve_forever()

