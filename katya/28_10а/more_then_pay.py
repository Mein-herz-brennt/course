import json
import datetime
import xml.etree.ElementTree as Et


class MoreThanPay:
    def __init__(self, filename1, filename2, filename3, filename4):
        self.tree1 = Et.ElementTree(file=filename1)
        self.tree1 = Et.ElementTree(file=filename1)
        self.tree1 = Et.ElementTree(file=filename1)
        self.tree1 = Et.ElementTree(file=filename1)
        self.filename2 = filename2
        self.filename3 = filename3
        self.filename4 = filename4

    def add_new_client(self, name, address, client_id):
        inf = {"id": client_id,
               "name": name,
               "address": address}
        adder(self.filename1, inf)

    def add_product(self, product_id, name, unit, price):
        inf = {"id": product_id,
               "name": name,
               "unit": unit,
               "price": price}
        adder(self.filename2, inf)

    def add_number(self, num_id, no, client_id):
        date = str(datetime.date.today())
        inf = {"id": num_id,
               "no": no,
               "date": date,
               "client_id": client_id}
        adder(self.filename3, inf)

    def add_payed(self, l_id, p_id, quantity):
        inf = {"l_id": l_id,
               "p_id": p_id,
               "quantity": quantity}
        adder(self.filename4, inf)
        return "Рахунок успішно додано!"

    def get_currencies(self):
        inf = reader(self.filename1)
        return [i["name"] for i in inf]

    def result(self, name: str):
        payed = {}
        client = {}
        number = {}
        inf_client = reader(self.filename1)  # "clients.json"
        inf_product = reader(self.filename2)  # "products.json"
        inf_number = reader(self.filename3)  # "number.json"
        inf_payed = reader(self.filename4)  # "payed.json"
        res_lst = []
        for i in inf_client:
            if i["name"] == name:
                res_lst.append(i)
                client = i
        for i in inf_number:
            if i["client_id"] == client["id"]:
                res_lst.append(i)
                number = i
        for i in inf_payed:
            if i["l_id"] == number["id"]:
                res_lst.append(i)
                payed = i
        for i in inf_product:
            if i["id"] == payed["p_id"]:
                res_lst.append(i)
        with open("result.json", "w", encoding="utf-8") as file:
            json.dump(res_lst, file, indent=3, ensure_ascii=False)
        return "result.json"

# if __name__ == '__main__':
#     cls = MoreThanPay("clients.json", "products.json", "number.json", "payed.json")
#     cls.add_new_client("Доміно", "domino@gmail.com", "C01")
#     cls.add_new_client("Кондор", "condor@gmail.com", "C02")
#     cls.add_product("P01", "Олівець", ".шт", "2.5")
#     cls.add_product("P02", "Ручка кулькова", ".шт", "2.4")
#     cls.add_number("I01", "253", "C01")
#     cls.add_number("I02", "255", "C02")
#     cls.add_payed("I02", "P01", "250")
#     cls.add_payed("I02", "P02", "150")
