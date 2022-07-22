import sqlite3


class Room:
    def __init__(self):
        self.conn = sqlite3.connect("HOTEL.db")
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

    def add_room(self, type_room: str, room_number: int, pay_for_day: int) -> str:
        self.cursor.execute(f"""INSERT INTO rooms VALUES (?,?,?)""", (type_room, room_number, pay_for_day))
        self.conn.commit()
        return f"Кімнату успішно додано!"

    def get_info_about_room(self, room: int) -> dict:
        room_info = self.cursor.execute(f"""SELECT * FROM rooms WHERE room_number = '{room}'""").fetchone()
        return {"type": room_info[0],
                "pay_day": room_info[2],
                "room": room_info[1]}

    def get_currency(self) -> list:
        rooms_info = self.cursor.execute(f"""SELECT * FROM rooms""").fetchall()
        return [i[1] for i in rooms_info]


class User:
    def __init__(self):
        self.conn = sqlite3.connect("HOTEL.db")
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

    def add_user(self, pib: str, room_number: int, days: int) -> str:
        pay_for_room = int(Room().get_info_about_room(room_number)["pay_day"]) * int(days)
        self.cursor.execute(f"""INSERT INTO users VALUES (?,?,?,?)""", (pib, room_number, days, pay_for_room))
        self.conn.commit()
        return "Користувача успішно додано!"

    def pay_for_one(self, room: int) -> str:
        user_pay = self.cursor.execute(F"""SELECT * FROM users WHERE room_number = '{room}'""").fetchone()
        return f"Гість: {user_pay[0]}, Повинен заплатити: {str(user_pay[3])}грн"

    def pay_for_all(self) -> str:
        users = self.cursor.execute(f"""SELECT * FROM users""").fetchall()
        all_pay = [user[3] for user in users]
        return f"Кожен повинен заплатити: {str(sum(all_pay) / len(all_pay))}грн"

    def delete_room(self, room_number) -> str:
        self.cursor.execute(f"""DELETE FROM users WHERE room_number = '{room_number}'""")
        self.conn.commit()
        return "Номер успішно звільнено!"

    def update_info_about_user(self, name: str, room: int, days: int) -> str:
        pay_for_room = int(Room().get_info_about_room(room)["pay_day"]) * int(days)
        self.cursor.execute(f"""UPDATE users SET days = ?, pay = ? WHERE name = ? and room_number = ?""",
                            (days, pay_for_room, name, room))
        self.conn.commit()
        return "Інформацію про користувача оновлено!"

    def get_cur(self) -> list:
        users = self.cursor.execute(f"""SELECT * FROM users""").fetchall()
        return [user[0] for user in users]
