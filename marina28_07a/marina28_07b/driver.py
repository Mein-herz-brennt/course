from datetime import date
import xml.etree.ElementTree as Et


#
# driver.xml structure
#
# <Drivers>
#   <Driver>
#       <pib>name</pib>
#       <fee_per_km>price</fee_per_km>
#       <load_capacity>num</load_capacity>
#   </Driver>
# </Drivers>
#
#
# waybills.xml structure
#
# <Waybills>
#   <Waybill>
#       <pib>name</pib>
#       <date>datetime</date>
#       <km>num</km>
#   </Waybill>
# </Waybills>
#

class Driver:
    def __init__(self):
        self.driver_et = Et.ElementTree(file="driver.xml")
        self.driver_root = self.driver_et.getroot()
        self.waybills_et = Et.ElementTree(file="waybills.xml")
        self.waybills_root = self.waybills_et.getroot()

    def add_driver(self, pib: str, fee_per_ton_km: str, load_capacity: str):
        element = Et.Element("Driver")
        Et.SubElement(element, 'pib').text = pib
        Et.SubElement(element, 'fee_per_km').text = fee_per_ton_km
        Et.SubElement(element, 'load_capacity').text = load_capacity
        self.driver_root.append(element)
        self.driver_et.write("driver.xml", encoding="utf-8")
        return "Водія додано!"

    def get_currencies(self):
        currencies = []
        for child in self.driver_root:
            pib = child.find("pib").text
            currencies.append(pib)
        return currencies

    def add_waybill(self, pib: str, date, km):
        element = Et.Element("Waybill")
        Et.SubElement(element, 'pib').text = pib
        Et.SubElement(element, 'date').text = date
        Et.SubElement(element, 'km').text = km
        self.waybills_root.append(element)
        self.waybills_et.write("waybills.xml", encoding="utf-8")
        return "Маршрутний лист успішно додано!"

    def pay_for_km(self, pib, date1, date2):
        date1 = date1.split("-")
        date2 = date2.split("-")
        start = date(int(date1[0]), int(date1[1]), int(date1[2]))
        end = date(int(date2[0]), int(date2[1]), int(date2[2]))
        all_waybills_of_this_man = []
        for child in self.driver_root:
            name = child.find("pib").text
            fee = int(child.find("fee_per_km").text)
            capacity = int(child.find("load_capacity").text)
            if name == pib:
                for children in self.waybills_root:
                    if children.find("pib").text == pib:
                        date3 = children.find("date").text.split("-")
                        date_now = date(int(date3[0]), int(date3[1]), int(date3[2]))
                        if start <= date_now <= end:
                            all_waybills_of_this_man.append(int(children.find("km").text))
                pay = 0
                for i in all_waybills_of_this_man:
                    pay += fee * capacity * i
                return pay



