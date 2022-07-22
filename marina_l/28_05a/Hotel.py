import json


def reader(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        text = json.load(file)
    return text


def adder(filename: str, info):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(info, file, indent=3)


class Room:

    def add_room(self, type_room: str, room_number: str, pay_for_day: str):
        inf = reader("rooms.json")
        inf.append({"type": type_room,
                    "pay_day": pay_for_day,
                    "room": room_number})
        adder("rooms.json", inf)
        return f"Кімнату успішно додано!"

    def get_info_about_room(self, room):
        inf = reader("rooms.json")
        for i in inf:
            if i["room"] == room:
                return i

    def get_currency(self):
        inf = reader("rooms.json")
        rooms = []
        for i in inf:
            rooms.append(i["room"])
        return rooms


class User:
    def add_user(self, pib: str, room_number: str, days: str):
        pay_for_room = int(Room().get_info_about_room(room_number)["pay_day"]) * int(days)
        inf = reader("users.json")
        inf.append({"pib": pib,
                    "room": room_number,
                    "days": days,
                    "pay": pay_for_room})
        adder("users.json", inf)
        return "Користувача успішно додано!"

    def pay_for_one(self, room: str):
        inf = reader("users.json")
        for i in inf:
            if i["room"] == room:
                return f"Гість: {i['pib']}, Повинен заплатити: {str(i['pay'])}грн"

    def pay_for_all(self):
        inf = reader("users.json")
        all_pay = []
        for i in inf:
            all_pay.append(i["pay"])
        return f"Кожен повинен заплатити: {str(sum(all_pay) / len(all_pay))}грн"
