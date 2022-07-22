import sqlite3


# Створення бази данних

# conn = sqlite3.connect("tovaru.db")
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE Providers
#                   (name text, phone text)
#                """)
# cursor.execute("""CREATE TABLE  Tovaru
#                   (name_provider text, tovar_name text, info_about text)
#                """)

class Goods:
    def __init__(self):
        self.conn = sqlite3.connect("tovaru.db")
        self.cursor = self.conn.cursor()

    def add_supplier(self, name: str, phone_number: str):
        self.cursor.execute(f"INSERT INTO Providers VALUES ('{name}','{phone_number}')")
        self.conn.commit()
        return "Постачальника успішно додано!"

    def add_goods(self, name: str, tovar: str, about: str):
        inf = [(name, tovar, about)]
        self.cursor.executemany("INSERT INTO Tovaru VALUES (?,?,?)", inf)
        self.conn.commit()
        return "Товар успішно додано!"

    def get_tovar_by_provider_name(self, name: str):
        self.conn.row_factory = sqlite3.Row
        goods = self.cursor.execute(
            f"SELECT * FROM Tovaru WHERE name_provider='{name}'").fetchall()
        provider = {"provider": name,
                    "tovaru": []}

        for i in goods:
            provider["tovaru"].append({"tovar": i[1], "opus": i[2]})

        return provider

    def get_provider_by_name(self, name: str):
        self.conn.row_factory = sqlite3.Row
        supplier = self.cursor.execute(
            f"SELECT * FROM Providers WHERE name='{name}'").fetchall()
        return supplier

    def get_provider_by_tovar_name(self, goods_name: str):
        self.conn.row_factory = sqlite3.Row
        goods = self.cursor.execute(
            f"SELECT * FROM Tovaru WHERE tovar_name='{goods_name}'").fetchall()
        suppliers = {"tovar": goods_name,
                     "providers": []}

        for i in goods:
            suppliers["providers"].append(i[0])
        return suppliers


if __name__ == '__main__':
    go = Goods()
    print(go.add_supplier("Петро", "2423423434"))
    print(go.add_goods("Петро", "Цибуля", "цибуля зелена"))
    print(go.get_provider_by_name("Петро"))
    print(go.get_tovar_by_provider_name("Петро"))
    print(go.get_provider_by_tovar_name("Цибуля"))
