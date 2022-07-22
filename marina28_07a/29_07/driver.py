import sqlite3
from datetime import date

# conn = sqlite3.connect("drivers.db")
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE drivers
#                   (name text, fee_per_ton_km int, load_capacity int)
#                """)
# cursor.execute("""CREATE TABLE waybills
#                   (name text, date text, km int)
#                """)


class Driver:
    def __init__(self):
        self.conn = sqlite3.connect("drivers.db")
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

    def add_driver(self, pib: str, fee_per_ton_km: int, load_capacity1: int):
        self.cursor.execute(f"""INSERT INTO drivers VALUES (?,?,?)""", (pib, fee_per_ton_km, load_capacity1))
        self.conn.commit()
        return "Водія додано!"

    def get_currencies(self):
        cur = self.cursor.execute("""SELECT * FROM drivers""").fetchall()
        al_in = []
        for cr in cur:
            al_in.append(cr[0])
        return al_in

    def add_waybill(self, pib: str, date_now: str, km):
        information = (pib, date_now, km)
        self.cursor.execute(f"""INSERT INTO waybills VALUES (?,?,?)""", information)
        self.conn.commit()
        return "Маршрутний лист успішно додано!"

    def delete_waybill(self, name: str, date_now: str):
        self.cursor.execute(f"""DELETE FROM waybills WHERE name = ? and date = ?""", (name, date_now))
        self.conn.commit()
        return "Маршрутний лист успішно видалено!"

    def update_waybill(self, name: str, date_now: str, new_km: int):
        sql = f"""
                UPDATE waybills 
                SET km = ?
                WHERE name = ? and date = ?
                """
        self.cursor.execute(sql, (new_km, name, date_now))
        self.conn.commit()
        return "Зміни внесено успішно!"

    def pay_for_km(self, pib, date1, date2):
        global fee_per_km, load_capacity
        date1 = date1.split("-")
        date2 = date2.split("-")
        start = date(int(date1[0]), int(date1[1]), int(date1[2]))
        end = date(int(date2[0]), int(date2[1]), int(date2[2]))
        all_waybills_of_this_man = []
        inf1 = self.cursor.execute(f"""SELECT * FROM drivers WHERE name = '{pib}'""").fetchone()
        inf2 = self.cursor.execute(f"""SELECT * FROM waybills WHERE name = '{pib}'""").fetchall()
        fee_per_km = inf1[1]
        load_capacity = inf1[2]
        for i in inf2:
            date3 = i[1].split("-")
            date_now = date(int(date3[0]), int(date3[1]), int(date3[2]))
            if start <= date_now <= end:
                all_waybills_of_this_man.append(i)
        pay = 0
        for i in all_waybills_of_this_man:
            pay += fee_per_km*load_capacity*int(i[2])
        return pay
