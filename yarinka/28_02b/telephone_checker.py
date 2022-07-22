import xml.etree.ElementTree as Et


class FriendPhones:
    def __init__(self):
        self.et = Et.ElementTree(file="friends.xml")
        self.root = self.et.getroot()

    def new_friend(self, name, phone):
        element = Et.Element("Friend")
        Et.SubElement(element, 'name').text = name
        Et.SubElement(element, 'phone').text = phone
        self.root.append(element)
        self.et.write("friends.xml", encoding="utf-8")
        return "Друга успішно додано!"

    def change_friend_name(self, new_name, phone):
        for child in self.root:
            if child.find("phone").text == phone:
                self.root.remove(child)
        element = Et.Element("Friend")
        Et.SubElement(element, 'name').text = new_name
        Et.SubElement(element, 'phone').text = phone
        self.root.append(element)
        self.et.write("friends.xml", encoding="utf-8")
        return "І'мя друга змінено!"

    def change_friend_phone(self, name, new_phone):
        for child in self.root:
            if child.find("name").text == name:
                self.root.remove(child)
        element = Et.Element("Friend")
        Et.SubElement(element, 'name').text = name
        Et.SubElement(element, 'phone').text = new_phone
        self.root.append(element)
        self.et.write("friends.xml", encoding="utf-8")
        return "Номер друга змінено!"

    def find_friend(self, name, phone):
        for child in self.root:
            friend_name = child.find("name").text
            friend_phone = child.find("phone").text
            if friend_name == name or friend_phone == phone:
                return f"Ім'я: {friend_name}, Номер: {friend_phone}"
            else:
                return "Вибачте та у вас нема такого друга!"
