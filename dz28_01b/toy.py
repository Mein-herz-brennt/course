import xml.etree.ElementTree as Et


class Toy:
    def __init__(self, filename: str):  # filename it's name our xml file in format "file.xml"
        self.et = Et.ElementTree(file=filename)
        self.root = self.et.getroot()

    def get_all_info_about(self):
        all_info = []
        # info_about_toy = {"name":"",
        #                   "years":"",
        #                   "price":""}
        for child in self.root:
            name = child.find("title").text
            years = child.find("years").text
            price = child.find("price").text
            info_about_toy = {"name": name,
                              "years": years,
                              "price": price}
            all_info.append(info_about_toy)
        return all_info

    def find_toy_by_name(self, name: str):
        all_info = self.get_all_info_about()
        toys_list = []
        try:
            for i in all_info:
                if i["name"] == name:
                    toys_list.append(i)
            return toys_list
        except Exception as e:
            print(f"Exception --> {e}")
            return "Sorry but we don't have this toy"

    def find_by_min_and_max_price(self, min_price, max_price):
        all_info = self.get_all_info_about()
        toys_list = []
        try:
            for i in all_info:
                if int(min_price) <= int(i["price"]) <= int(max_price):
                    toys_list.append(i)
            return toys_list
        except Exception as e:
            print(f"Exception --> {e}")
            return "Sorry but we don't have toys in this price"

    def find_toys_by_years(self, years=0):
        year = int(years)
        all_info = self.get_all_info_about()
        toys_list = []
        # try:
        for i in all_info:
            alder = i["years"].split("-")
            if alder[1] != "+":
                if int(alder[0]) <= year <= int(alder[1]):
                    toys_list.append(i)
            else:
                if int(alder[0]) <= year:
                    toys_list.append(i)
        return toys_list
        # except Exception as e:
        #     print(f"Exception --> {e}")
        #     return "Sorry but we don't have toys for this age"

    def get_all_toys_names(self):
        all_info = self.get_all_info_about()
        names = [i["name"] for i in all_info]
        return names

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

    def toys_xml(self):
        tree = Et.ElementTree(file="result.xml")
        root = tree.getroot()
        element = Et.Element("Toys")
        root = element
        tree.write("result.xml", encoding="utf-8", xml_declaration=True)

    def result_xml(self, toys: list) -> str:
        if self.remover():
            self.toys_xml()
            tree = Et.ElementTree(file="result.xml")
            root = tree.getroot()
            try:
                for i in toys:
                    sub = Et.Element("Toy")
                    Et.SubElement(sub, "title").text = i["name"]
                    Et.SubElement(sub, "age").text = i["years"]
                    Et.SubElement(sub, "price").text = i["price"]
                    root.append(sub)
                tree.write("result.xml", encoding="utf-8", xml_declaration=True)
                return "result.xml"
            except Exception:
                return "bad code"
        else:
            return "bad remove"




