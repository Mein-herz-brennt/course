import sqlite3


class FriendBook:

    def __init__(self):
        self.conn = sqlite3.connect("friends.db")
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

    def new_friend(self, name, phone):
        self.cursor.execute(f"""INSERT INTO friends VALUES (?,?)""", (name, phone))
        self.conn.commit()
        return "Друга успішно додано!"

    def change_friend_name(self, new_name, phone):
        self.cursor.execute(f"""UPDATE friends SET name = ? WHERE phone = ?""", (new_name, phone))
        self.conn.commit()
        return "І'мя друга змінено!"

    def change_friend_phone(self, name, new_phone):
        self.cursor.execute(f"""UPDATE friends SET phone = ? WHERE name = ?""", (new_phone, name))
        self.conn.commit()
        return "Номер друга змінено!"

    def find_friend(self, name, phone):
        try:
            all_info = self.cursor.execute(f"""SELECT * FROM friends WHERE name = ? or phone = ?""", (name, phone)).fetchall()
            friends = []
            for i in all_info:
                friends.append(f"Ім'я: {i[0]}, Номер: {i[1]}")
            return friends
        except Exception:
            return "Вибачте та у вас нема такого друга!"

    def delete_friend(self, name, phone):
        self.cursor.execute(f"""DELETE FROM friends WHERE name = ? and phone = ?""", (name, phone))
        self.conn.commit()
        return "Видалення успішне!"
