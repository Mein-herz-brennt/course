import xml.etree.ElementTree as Et


class Room:
    def __init__(self):
        self.et = Et.ElementTree(file="rooms.xml")
        self.root = self.et.getroot()

    def add_room(self, type_room: str, room_number: str, pay_for_day: str):
        element = Et.Element("Room")
        Et.SubElement(element, 'type_room').text = type_room
        Et.SubElement(element, 'room_number').text = room_number
        Et.SubElement(element, 'pay_for_day').text = pay_for_day
        self.root.append(element)
        self.et.write("rooms.xml", encoding="utf-8")
        return f"Кімнату успішно додано!"

    def get_info_about_room(self, room):
        for child in self.root:
            if child.find("room_number").text == room:
                return child.find("pay_for_day").text

    def get_currency(self):
        rooms = []
        for child in self.root:
            rooms.append(child.find("room_number").text)
        return rooms


class User:
    def __init__(self):
        self.et = Et.ElementTree(file="users.xml")
        self.root = self.et.getroot()

    def add_user(self, pib: str, room_number: str, days: str):
        pay_for_room = int(Room().get_info_about_room(room_number)) * int(days)
        element = Et.Element("User")
        Et.SubElement(element, 'pib').text = pib
        Et.SubElement(element, 'room_number').text = room_number
        Et.SubElement(element, 'days').text = days
        Et.SubElement(element, 'pay_for_room').text = str(pay_for_room)
        self.root.append(element)
        self.et.write("users.xml", encoding="utf-8")
        return "Користувача успішно додано!"

    def pay_for_one(self, room: str):
        for child in self.root:
            if child.find("room_number").text == room:
                return f"Гість: {child.find('pib').text}, Повинен заплатити: {child.find('pay_for_room').text}грн"

    def pay_for_all(self):
        all_pay = []
        for child in self.root:
            all_pay.append(int(child.find('pay_for_room').text))
        return f"Кожен повинен заплатити: {str(sum(all_pay) / len(all_pay))}грн"
