import xml.etree.ElementTree as Et
import datetime


class MoreThanPay:
    def __init__(self, filename1, filename2, filename3, filename4):
        self.tree1 = Et.ElementTree(file=filename1)
        self.tree2 = Et.ElementTree(file=filename2)
        self.tree3 = Et.ElementTree(file=filename3)
        self.tree4 = Et.ElementTree(file=filename4)
        self.root1 = self.tree1.getroot()
        self.root2 = self.tree2.getroot()
        self.root3 = self.tree3.getroot()
        self.root4 = self.tree4.getroot()
        self.filename1 = filename1
        self.filename2 = filename2
        self.filename3 = filename3
        self.filename4 = filename4

    def add_new_client(self, name, address, client_id):
        elem = Et.Element("User")
        Et.SubElement(elem, "client_id").text = client_id
        Et.SubElement(elem, "name").text = name
        Et.SubElement(elem, "address").text = address
        self.root1.append(elem)
        self.tree1.write(self.filename1, encoding="utf-8", xml_declaration=True)
        # inf = {"id": client_id,
        #        "name": name,
        #        "address": address}
        # adder(self.filename1, inf)

    def add_product(self, product_id, name, unit, price):
        elem = Et.Element("Product")
        Et.SubElement(elem, "product_id").text = product_id
        Et.SubElement(elem, "name").text = name
        Et.SubElement(elem, "unit").text = unit
        Et.SubElement(elem, "price").text = price
        self.root2.append(elem)
        self.tree2.write(self.filename2, encoding="utf-8", xml_declaration=True)
        # inf = {"id": product_id,
        #        "name": name,
        #        "unit": unit,
        #        "price": price}
        # adder(self.filename2, inf)

    def add_number(self, num_id, no, client_id):
        date = str(datetime.date.today())
        elem = Et.Element("Number")
        Et.SubElement(elem, "num_id").text = num_id
        Et.SubElement(elem, "no").text = no
        Et.SubElement(elem, "date").text = date
        Et.SubElement(elem, "client_id").text = client_id
        self.root3.append(elem)
        self.tree3.write(self.filename3, encoding="utf-8", xml_declaration=True)
        # inf = {"id": num_id,
        #        "no": no,
        #        "date": date,
        #        "client_id": client_id}
        # adder(self.filename3, inf)

    def add_payed(self, l_id, p_id, quantity):
        elem = Et.Element("Payed")
        Et.SubElement(elem, "l_id").text = l_id
        Et.SubElement(elem, "p_id").text = p_id
        Et.SubElement(elem, "quantity").text = quantity
        self.root4.append(elem)
        self.tree4.write(self.filename4, encoding="utf-8", xml_declaration=True)
        # inf = {"l_id": l_id,
        #        "p_id": p_id,
        #        "quantity": quantity}
        # adder(self.filename4, inf)
        return "Рахунок успішно додано!"

    def get_currencies(self):
        # inf = reader(self.filename1)
        return [i.find("name").text for i in self.root1]

    def remover(self):
        try:
            tree = Et.ElementTree(file="result.xml")
            root = tree.getroot()
            for child in list(root):
                root.remove(child)
            tree.write("result.xml", encoding="utf-8", xml_declaration=True)
            return True
        except Exception:
            return False

    def res_xml(self):
        tree = Et.ElementTree(file="result.xml")
        element = Et.Element("Scores")
        root = element
        tree.write("result.xml", encoding="utf-8", xml_declaration=True)

    def result(self, name: str):
        if self.remover():
            self.res_xml()
            tree = Et.ElementTree(file="result.xml")
            root = tree.getroot()
            # elem = Et.Element("Score")
            payed = ""
            client = ""
            number = ""
            # inf_client = reader(self.filename1)  # "clients.json"
            # inf_product = reader(self.filename2)  # "products.json"
            # inf_number = reader(self.filename3)  # "number.json"
            # inf_payed = reader(self.filename4)  # "payed.json"
            # res_lst = []
            for i in self.root1:
                if i.find("name").text == name:
                    client = i.find("client_id").text
                    root.append(i)
            for i in self.root3:
                if i.find("client_id").text == client:
                    root.append(i)
                    number = i.find("num_id").text
            for i in self.root4:
                if i.find("l_id").text == number:
                    root.append(i)
                    payed = i.find("p_id").text
            for i in self.root2:
                if i.find("product_id").text == payed:
                    root.append(i)
            tree.write("result.xml", encoding="utf-8", xml_declaration=True)
            # with open("result.json", "w", encoding="utf-8") as file:
            #     json.dump(res_lst, file, indent=3, ensure_ascii=False)
            return "result.xml"


# if __name__ == '__main__':
    # cls = MoreThanPay("clients.xml", "products.xml", "number.xml", "payed.xml")
    # cls.add_new_client("Доміно", "domino@gmail.com", "C01")
    # cls.add_new_client("Кондор", "condor@gmail.com", "C02")
    # cls.add_product("P01", "Олівець", ".шт", "2.5")
    # cls.add_product("P02", "Ручка кулькова", ".шт", "2.4")
    # cls.add_number("I01", "253", "C01")
    # cls.add_number("I02", "255", "C02")
    # cls.add_payed("I02", "P01", "250")
    # cls.add_payed("I01", "P02", "150")
    # a = MoreThanPay("clients.xml", "products.xml", "number.xml", "payed.xml")
    # print(a.result("Доміно"))
