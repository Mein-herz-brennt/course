import sqlite3
import json
import os
import random


def new_datebase():
    conn = sqlite3.connect("detail_magazine.db")
    cursor = conn.cursor()

    cursor.execute(f"""CREATE TABLE detail (name text, car_mark text, car_model text, category text, date text, 
                    prise int, code int)""")
    cursor.execute(f"""CREATE TABLE car (mark text, model text, date text)""")
    cursor.execute(f"""CREATE TABLE files (code int, filename text)""")


class WorkWithJSON:
    def new_json_file(self, filename: str, info: list):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(info, file, ensure_ascii=False)
        return filename

    def delete_file(self, filename: str):
        if filename.endswith(".json"):
            os.remove(filename)
            return 0
        else:
            raise ValueError("the file must be in .json format")


class WorkWithDB:
    def __init__(self):
        self.conn = sqlite3.connect("detail_magazine.db")
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row
        self._work_with_json = WorkWithJSON()
        self.code = 0

    def add_car(self, mark: str, model: str, date: str) -> str:
        self.cursor.execute(f"""INSERT INTO car VALUES (?,?,?)""",
                            (mark, model, date))
        self.conn.commit()
        return f"Машину марки: {mark} успішно додано!"

    def add_detail(self, name: str, car_mark: str, car_model: str, category: str, date: str, prise: int) -> str:
        self.code = random.randint(10**6, 10**7)
        self.cursor.execute(f"""INSERT INTO detail VALUES (?,?,?,?,?,?,?)""",
                            (name, car_mark, car_model, category, date, prise, self.code))
        self.conn.commit()
        return f"Деталь: {name} успішно додано!"

    def add_file(self, filename: str) -> int:
        self.cursor.execute(f"""INSERT INTO files VALUES (?,?)""", (self.code, filename))
        self.conn.commit()
        return self.code

    def update_car(self, mark: str, model: str, date: str) -> str:
        sql = f"""UPDATE car 
        SET date = ? 
        WHERE mark = ? and model = ?"""
        self.cursor.execute(sql, (date, mark, model))
        self.conn.commit()
        return f"Інформацію про машину марки: {mark} успішно оновлено!"

    def update_detail(self, name: str, car_mark: str, car_model: str, category: str, date: str, prise: int) -> str:
        sql = f"""UPDATE detail SET category = ?, prise = ?, name = ? WHERE car_mark = ? and car_model = ? and date = ?"""
        self.cursor.execute(sql, (category, prise, name, car_mark, car_model, date))
        self.conn.commit()
        return f"Інформацію про деталь успішно поновлено!"

    def get_info_about_details_by_name(self, name: str) -> tuple:
        file = f"file{random.randint(10**5, 10**6)}.json"
        info = self.cursor.execute(f"""SELECT * FROM detail WHERE name = ?""", (name,)).fetchall()
        gen = [{"name": i[0], "car_mark": i[1], "car_model": i[2], "date": i[4], "category": i[3], "prise": i[5]} for i
               in info]
        filename = self._work_with_json.new_json_file(file, gen)
        code = self.add_file(filename)
        return code, filename

    def get_info_about_details_by_category(self, category: str) -> tuple:
        file = f"file{random.randint(10 ** 5, 10 ** 6)}.json"
        info = self.cursor.execute(f"""SELECT * FROM detail WHERE category = ?""", (category,)).fetchall()
        gen = [{"name": i[0], "car_mark": i[1], "car_model": i[2], "date": i[4], "category": i[3], "prise": i[5]} for i
               in info]
        filename = self._work_with_json.new_json_file(file, gen)
        code = self.add_file(filename)
        return code, filename

    def get_info_about_file(self, code: int) -> tuple:
        info = self.cursor.execute(f"""SELECT * FROM files WHERE code = ?""",
                                   (code,)).fetchone()
        return info

    def get_all_details_names(self) -> list:
        info = self.cursor.execute(f"""SELECT * FROM detail""").fetchall()
        return [i[0] for i in info]

    def get_all_car_marks(self) -> list:
        info = self.cursor.execute(f"""SELECT * FROM car""").fetchall()
        return [i[1] for i in info]

    def get_all_files(self) -> list:
        filenames = self.cursor.execute(f"""SELECT * FROM files""")
        return [i[2] for i in filenames]

    def delete_car(self, model: str, mark: str, date: str) -> str:
        self.cursor.execute(f"""DELETE FROM car WHERE mark = ? and model = ? and date = ?""",
                            (mark, model, date))
        self.cursor.execute(f"""DELETE FROM detail WHERE car_mark = ? and car_model = ? and date = ?""",
                            (mark, model, date))
        self.conn.commit()
        return f"Машину: {mark} успішно видалено!"

    def delete_detail(self, name: str, model: str, mark: str, date: str) -> str:
        self.cursor.execute(f"""DELETE FROM detail WHERE name = ? and car_mark = ? and car_model = ? and date = ?""",
                            (name, mark, model, date))
        self.conn.commit()
        return f"Деталь: {name} успішно видалено!"

    def get_all_car_models(self):
        info = self.cursor.execute(f"""SELECT * FROM car""").fetchall()
        return [i[0] for i in info]


if __name__ == '__main__':
    new_datebase()
