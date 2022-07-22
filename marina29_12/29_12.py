import sqlite3


# Створення бази данних

# conn = sqlite3.connect("goods.db")
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE Suppliers
#                   (name text, phone text)
#                """)
# cursor.execute("""CREATE TABLE  Goods
#                   (name_supplier text, goods_name text, info_about text)
#                """)

class Goods:
    def __init__(self):
        self.conn = sqlite3.connect("goods.db")
        self.cursor = self.conn.cursor()

    def add_supplier(self, name: str, phone: str):
        self.cursor.execute(f"INSERT INTO Suppliers VALUES ('{name}','{phone}')")
        self.conn.commit()
        return "Постачальника успішно додано!"

    def add_goods(self, name: str, goods_name: str, about: str):
        inf = [(name, goods_name, about)]
        self.cursor.executemany("INSERT INTO Goods VALUES (?,?,?)", inf)
        self.conn.commit()
        return "Товар успішно додано!"

    def get_goods_by_supplier_name(self, name: str):
        self.conn.row_factory = sqlite3.Row
        goods = self.cursor.execute(
            f"SELECT * FROM Goods WHERE name_supplier='{name}'").fetchall()
        supplier = {"name": name,
                    "goods": []}

        for i in goods:
            supplier["goods"].append({"goods": i[1], "description": i[2]})

        return supplier

    def get_supplier_by_name(self, name: str):
        self.conn.row_factory = sqlite3.Row
        supplier = self.cursor.execute(
            f"SELECT * FROM Suppliers WHERE name='{name}'").fetchall()
        return supplier

    def get_supplier_by_goods_name(self, goods_name: str):
        self.conn.row_factory = sqlite3.Row
        goods = self.cursor.execute(
            f"SELECT * FROM Goods WHERE goods_name='{goods_name}'").fetchall()
        suppliers = {"goods": goods_name,
                     "suppliers": []}

        for i in goods:
            suppliers["suppliers"].append(i[0])
        return suppliers


if __name__ == '__main__':
    go = Goods()
    print(go.add_supplier("Андрій", "0429489348"))
    print(go.add_goods("Андрій", "Крісло", "Крісло на колесах комп'ютерне"))
    print(go.get_supplier_by_name("Андрій"))
    print(go.get_goods_by_supplier_name("Андрій"))
    print(go.get_supplier_by_goods_name("Крісло"))