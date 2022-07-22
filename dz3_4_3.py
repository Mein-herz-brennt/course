def writer(text, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(text)


def reader(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.readlines()
    return text


class Goods:
    def __init__(self, category_of_goods):
        self.category = category_of_goods

    def get_info_about_goods(self, name_of_goods):
        pass

    def pay_for_goods(self, name_of_goods):
        pass


class ChemicalGoods(Goods):
    def __init__(self, all_info_about_goods: list):
        super().__init__("chemical")
        self.name_of_goods = all_info_about_goods[0]
        self.date_to_check = all_info_about_goods[1]
        self.pay = all_info_about_goods[2]
        inf = reader("goods.txt")
        text = f"категорія товару: {self.category}, назва товару: {self.name_of_goods}, дата виготовлення: {self.date_to_check} , ціна товару: {self.pay}grn.\n"
        inf.append(text)
        writer(inf, "goods.txt")

    def get_info_about_goods(self, name_of_goods):
        text = reader("goods.txt")
        for i in text:
            if name_of_goods in i:
                return i

    def pay_for_goods(self, name_of_goods):
        text = reader("goods.txt")
        for i in range(len(text)):
            if name_of_goods in text[i]:
                pay = text[i].split(" ")[-1].lstrip("\n")
                text.pop(i)
                writer(text, "goods.txt")
                return f"назва товару: {name_of_goods} , ціна товару: {pay}"

    def backout_goods(self, name_of_goods, date_to_check, pay):
        text = reader("goods.txt")
        text.append(
            f"категорія товару: {self.category}, назва товару: {name_of_goods}, дата виготовлення: {date_to_check} , ціна товару: {pay}grn.\n")
        writer(text, "goods.txt")
        return f"Товар повернено!"


class FoodGoods(Goods):
    def __init__(self, all_info_about_goods: list):
        super().__init__("food")
        self.name_of_goods = all_info_about_goods[0]
        self.date_to_check = all_info_about_goods[1]
        self.pay = all_info_about_goods[3]
        self.date_to_backout = all_info_about_goods[2]
        inf = reader("goods.txt")
        text = f"категорія товару: {self.category}, назва товару: {self.name_of_goods}, дата виготовлення: {self.date_to_check}, дата придатності: {self.date_to_backout} , ціна товару: {self.pay}grn.\n"
        inf.append(text)
        writer(inf, "goods.txt")

    def get_info_about_goods(self, name_of_goods):
        text = reader("goods.txt")
        for i in text:
            if name_of_goods in i:
                return i

    def pay_for_goods(self, name_of_goods):
        text = reader("goods.txt")
        for i in range(len(text)):
            if name_of_goods in text[i]:
                pay = text[i].split(" ")[-1].lstrip("\n")
                text.pop(i)
                writer(text, "goods.txt")
                return f"назва товару: {name_of_goods} , ціна товару: {pay}"

    def backout_goods(self, name_of_goods, date_to_check, pay, date_to_backout=""):
        text = reader("goods.txt")
        text.append(
            f"категорія товару: {self.category}, назва товару: {name_of_goods}, дата виготовлення: {date_to_check}, дата придатності: {date_to_backout} , ціна товару: {pay}grn.\n")
        writer(text, "goods.txt")
        return f"Товар повернено!"


class ClothesGoods(Goods):
    def __init__(self, all_info_about_goods: list):
        super().__init__("clothes")
        self.name_of_goods = all_info_about_goods[0]
        self.date_to_check = all_info_about_goods[1]
        self.pay = all_info_about_goods[3]
        self.size = all_info_about_goods[2]
        inf = reader("goods.txt")
        text = f"категорія товару: {self.category}, назва товару: {self.name_of_goods}, дата виготовлення: {self.date_to_check}, розмір: {self.size} , ціна товару: {self.pay}grn.\n"
        inf.append(text)
        writer(inf, "goods.txt")

    def get_info_about_goods(self, name_of_goods):
        text = reader("goods.txt")
        for i in text:
            if name_of_goods in i:
                return i

    def pay_for_goods(self, name_of_goods):
        text = reader("goods.txt")
        for i in range(len(text)):
            if name_of_goods in text[i]:
                pay = text[i].split(" ")[-1].lstrip("\n")
                text.pop(i)
                writer(text, "goods.txt")
                return f"назва товару: {name_of_goods} , ціна товару: {pay}"

    def backout_goods(self, name_of_goods, date_to_check, pay, size=""):
        text = reader("goods.txt")
        text.append(
            f"категорія товару: {self.category}, назва товару: {name_of_goods}, дата виготовлення: {date_to_check}, розмір: {size} , ціна товару: {pay}grn.\n")
        writer(text, "goods.txt")
        return f"Товар повернено!"


if __name__ == '__main__':
    # перед запуском потрібно створити фойл "goods.txt"
    a = ChemicalGoods(["омивайка", "2022-12-17", "200"])
    b = FoodGoods(["булочка", "2022-04-28", "2022-04-30", "10"])
    c = ClothesGoods(["Черевики", "2020-08-25", "45", "1000"])
    print(b.backout_goods("булочка", "2022-04-28", "2022-04-30", "10"))
    print(a.pay_for_goods("омивайка"))
    print(c.get_info_about_goods("Черевики"))
