import sqlite3
import xml.etree.ElementTree as Et


# conn = sqlite3.connect("TOYS.db")
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE toys
#                   (title text, min_age text, max_age text, price int)
#                """)


class Toy:
    def __init__(self, filename: str):  # filename it's name our xml file in format "file.xml"
        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

    def add_toy(self, name: str, min_years: str, max_years: str, price: int) -> str:
        info = (name, min_years, max_years, price)
        self.cursor.execute(f"""INSERT INTO toys VALUES (?,?,?,?)""", info)
        self.conn.commit()
        return "Іграшку успішно додано!"

    def delete_toy(self, name: str) -> str:
        sql = f"""DELETE FROM toys WHERE title = '{name}'"""
        self.cursor.execute(sql)
        self.conn.commit()
        return "Іграшку успішно видалено!"

    def update_toy(self, name: str, min_years: str, max_years: str, price: int) -> str:
        sql = f"""
                UPDATE toys 
                SET min_age = ?, max_age = ?, price = ?
                WHERE title = ?
                """
        self.cursor.execute(sql, (min_years, max_years, price, name))
        self.conn.commit()
        return "Інформацію про іграшку успішно оновлено!"

    def get_all_info_about(self) -> list:
        all_info = []
        info = self.cursor.execute("SELECT * FROM toys").fetchall()
        for i in info:
            info_about_toy = {"name": i[0],
                              "years": i[1] + "-" + i[2],
                              "price": i[3]}
            all_info.append(info_about_toy)
        return all_info

    def find_toy_by_name(self, name: str):
        all_info = self.get_all_info_about()
        toys_list = []
        try:
            for i in all_info:
                if i["name"] == name:
                    toys_list.append(
                        f"""<p>Назва іграшки: {i['name']}, ціна: {i['price']}грн, вікові обмеження: {i['years']}</p>""")
            return toys_list
        except Exception as e:
            print(f"Exception --> {e}")
            return "Sorry but we don't have this toy"

    def find_by_min_and_max_price(self, min_price, max_price):
        all_info = self.get_all_info_about()
        toys_list = []
        try:
            for i in all_info:
                if int(min_price) <= int(i["price"]) <= int(max_price):
                    toys_list.append(
                        f"""<p>Назва іграшки: {i['name']}, ціна: {i['price']}грн, вікові обмеження: {i['years']}</p>""")
            return toys_list
        except Exception as e:
            print(f"Exception --> {e}")
            return "Sorry but we don't have toys in this price"

    def find_toys_by_years(self, years=0):
        year = int(years)
        all_info = self.get_all_info_about()
        toys_list = []
        # try:
        for i in all_info:
            alder = i["years"].split("-")
            if alder[1] != "+":
                if int(alder[0]) <= year <= int(alder[1]):
                    toys_list.append(
                        f"""<p>Назва іграшки: {i['name']}, ціна: {i['price']}грн, вікові обмеження: {i['years']}</p>""")
            else:
                if int(alder[0]) <= year:
                    toys_list.append(
                        f"""<p>Назва іграшки: {i['name']}, ціна: {i['price']}грн, вікові обмеження: {i['years']}</p>""")
        return toys_list
        # except Exception as e:
        #     print(f"Exception --> {e}")
        #     return "Sorry but we don't have toys for this age"

    def get_all_toys_names(self):
        info = self.cursor.execute("SELECT * FROM toys").fetchall()
        names = [i[0] for i in info]
        return names


if __name__ == '__main__':
    a = Toy("TOYS.db")
    print(a.update_toy("Лялька Barbie", "3", "16", 500))

    # print(a.find_toys_by_years("85"))
    # print(a.find_toy_by_name("Лялька Barbie"))
    # print(a.find_by_min_and_max_price("85", "700"))
