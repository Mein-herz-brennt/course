import sqlite3
import docx


def create_db():
    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()
    cursor.execute(f"""CREATE TABLE goods (name text, caption text, consignment text, category text, num int)""")
    cursor.execute(f"""CREATE TABLE storage (name text, address text, department text, shelf text, num int)""")
    cursor.execute(f"""CREATE TABLE stock (name text, caption text, address text, good text, num int)""")
    cursor.execute(f"""CREATE TABLE files (type_of text, name text, filename text)""")


class WorkWithDocx:
    pass


class WorkWithDB:
    def __init__(self):
        self.conn = sqlite3.connect("stock.db")
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

    def add_goods(self, name: str, caption: str, consignment: str, category: str, num: int):
        self.cursor.execute(f"""INSERT INTO goods VALUES (?,?,?,?,?)""", (name, caption, consignment, category, num))
        self.conn.commit()

    def add_storage(self, name_of_good: str, address: str, department: str, shelf: str, num: int):
        self.cursor.execute(f"""INSERT INTO storage VAlUES (?,?,?,?,?)""",
                            (name_of_good, address, department, shelf, num))
        self.conn.commit()

    def add_stock(self, name_of_good: str, caption: str, address: str, good: str, num: int):
        self.cursor.execute(f"""INSERT INTO stock VAlUES (?,?,?,?,?)""",
                            (name_of_good, caption, address, good, num))
        self.conn.commit()

    def add_file(self, appointment: str, name: str, filename: str):
        self.cursor.execute(f"""INSERT INTO files VALUES (?,?,?)""", (appointment, name, filename))
        self.conn.commit()

    def get_good_from_stock(self, good: str, address: str, num: int):
        goods_num = self.cursor.execute(f"""SELECT * FROM stock WHERE adress = ? and name = ?""",
                                        (address, good)).fetchall()
        self.cursor.execute(f"UPDATE stock SET num = ? WHERE address = ? and name = ?",
                            (goods_num[-1] - num, address, good))
        self.conn.commit()

    def get_good_by_category(self, category: str):
        goods = self.cursor.execute(f"""SELECT * FROM goods WHERE category = ?""", (category,)).fetchall()
        return goods

    def get_goods_by_like_name(self, name: str):
        goods = self.cursor.execute(f"""SELECT * FROM goods WHERE category LIKE %?%""", (name,)).fetchall()
        return goods

