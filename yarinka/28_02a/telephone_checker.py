import json


def reader(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        text = json.load(file)
    return text


def writer(text, filename: str):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(text, file, indent=3)


class FriendPhones:

    def new_friend(self, name, phone):
        new_friend = {"name": name, "phone": phone}
        information = reader("friends.json")
        information.append(new_friend)
        writer(information, "friends.json")
        return "Друга успішно додано!"

    def change_friend_name(self, new_name, phone):
        phone_book = reader("friends.json")
        for i in range(len(phone_book)):
            if phone_book[i]["phone"] == phone:
                phone_book[i]["name"] = new_name
                break
        writer(phone_book, "friends.json")
        return "І'мя друга змінено!"

    def change_friend_phone(self, name, new_phone):
        phone_book = reader("friends.json")
        for i in range(len(phone_book)):
            if phone_book[i]["name"] == name:
                phone_book[i]["phone"] = new_phone
                break
        writer(phone_book, "friends.json")
        return "Номер друга змінено!"

    def find_friend(self, name, phone):
        phone_book = reader("friends.json")
        for i in range(len(phone_book)):
            if phone_book[i]["name"] == name or phone_book[i]["phone"] == phone:
                return f"Ім'я: {phone_book[i]['name']}, Номер: {phone_book[i]['name']}"
            else:
                return "Вибачте та у вас нема такого друга!"
