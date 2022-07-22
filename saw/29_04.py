import sqlite3

#
# Створення бази данних
#
# conn = sqlite3.connect("utilities_payments.db")
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE companies
#                   (company_name text, score int)
#                """)
# cursor.execute("""CREATE TABLE none_payments_name
#                   (formal_name text, non_formal_name text)
#                """)
# cursor.execute("""CREATE TABLE payments
#                   (company text, non_formal_name text, payment_date text, to_pay text, payed_date text, payed text)
#                """)


class Payment:
    def __init__(self):
        self.conn = sqlite3.connect("utilities_payments.db")
        self.cursor = self.conn.cursor()

    def add_company(self, company_name: str, score: int):
        ing = (company_name, score)
        self.cursor.execute("INSERT INTO companies VALUES (?,?)", ing)
        self.conn.commit()
        return "Компанію успішно додано!"

    def add_non_formal_name_of_payment(self, formal_name: str, non_formal_name: str):
        self.cursor.execute(f"""INSERT INTO none_payments_name VALUES ('{formal_name}', '{non_formal_name}')""")
        self.conn.commit()
        return "Неформальну назву платежу успішно додано!"

    def add_payment(self, company: str, name_of_payment: str, payment_date: str, to_pay: str):  # date in format
        # year-month-date
        inf = (company, name_of_payment, payment_date, to_pay, "", "")
        self.cursor.execute(f"""INSERT INTO payments VALUES (?,?,?,?,?,?)""", inf)
        self.conn.commit()
        return "Інформацію про Платіж успішно додано"

    def pay(self, company: str, name_of_payment: str, date: str, payed: str):
        sql = f"""
        UPDATE payments 
        SET payed_date = ?, payed = ?
        WHERE company = ? and non_formal_name = ?
        """

        self.cursor.execute(sql, (date, payed, company, name_of_payment))
        self.conn.commit()
        return "Платіж проведено успішно!"

    def get_payment(self, date: str):  # date in format year-month
        self.conn.row_factory = sqlite3.Row
        payments = self.cursor.execute("SELECT * FROM payments").fetchall()
        payment = []
        for i in range(len(payments)):
            if payments[i][2].startswith(date):
                payment.append(payments[i])
        to_pay = sum([int(i[-3]) for i in payment])
        payed = sum([int(i[-1]) for i in payment])
        for i in payment:
            print(i)
        print("До сплати ->",  to_pay)
        print("Сплачено ->", payed)
        return payments, to_pay, payed


if __name__ == '__main__':
    a = Payment()
    print(a.add_company("У Степана", 19394943))
    print(a.add_non_formal_name_of_payment("Рахунок за газ", "За газ"))
    print(a.add_payment('Степана', "За газ", "2022-05-07", "200"))
    # print(a.pay('Степана', "За газ", "2022-05-12", "150"))
    # a.get_payment("2022-05")

