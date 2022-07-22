import sqlite3


# Створення бази данних

# conn = sqlite3.connect("houses.db")
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE houses
#                   (type_of text, adresa text, all_ploshcha real, room_count int)
#                """)
# cursor.execute("""CREATE TABLE rooms
#                   (type_of text, adresa text, pruznachenya text, ploshcha_room real)
#                """)


class Dim:
    def __init__(self):
        self.conn = sqlite3.connect("houses.db")
        self.cursor = self.conn.cursor()

    def add_object(self, type_of: str, adresa: str, ploshcha: float, room_count: int):
        inf = [(type_of, adresa, ploshcha, room_count)]
        self.cursor.executemany("INSERT INTO houses VALUES (?,?,?,?)", inf)
        self.conn.commit()
        return "Об'єкт успішно додано!"

    def add_room(self, type_of: str, adresa: str, pruznachenya: str, ploshcha_room: float):
        inf = [(type_of, adresa, pruznachenya, ploshcha_room)]
        self.cursor.executemany("INSERT INTO rooms VALUES (?,?,?,?)", inf)
        self.conn.commit()
        return "Кімнату успішно додано!"

    def get_info(self, type_of: str, ploshcha: float):
        self.conn.row_factory = sqlite3.Row
        objects = self.cursor.execute(
            f"SELECT * FROM houses WHERE all_ploshcha={ploshcha} and type_of='{type_of}'").fetchall()
        adresa = [i[1] for i in objects]
        all_rooms = []
        for i in adresa:
            rooms = self.cursor.execute(f"SELECT * FROM rooms WHERE adresa='{i}' and type_of='{type_of}'").fetchall()
            all_rooms.append(rooms)
        all_objects = []
        for i in range(len(objects)):
            objec = {"object": objects[i],
                     "rooms": all_rooms[i]}
            all_objects.append(objec)
        for i in all_objects:
            print(i)
        return all_objects


if __name__ == '__main__':
    obj = Dim()
    print(obj.add_object("Дім", "івана тополі 28", 36, 5))
    print(obj.add_room("Дім", "івана тополі 28", "Ванна", 6))
    obj.get_info("Дім", 36)
