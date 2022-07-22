import json
from datetime import date

# inf = [{"pib": "", "fee_per_km": "", "load_capacity": ""}]
# waybill = [{"pib": []}]


def reader(filename):
    with open(filename, "r") as file:
        info = json.load(file)
    return info


def adder(inf, filename: str):
    with open(filename, "w") as file:
        json.dump(inf, file, indent=3)


class Driver:
    def add_driver(self, pib: str, fee_per_ton_km: float, load_capacity: float):
        inf = reader("driver.json")
        inf.append({"pib": pib,
                    "fee_per_km": fee_per_ton_km,
                    "load_capacity": load_capacity})
        adder(inf, "driver.json")
        return "Водія додано!"

    def get_currencies(self):
        inf = reader("driver.json")
        pibs = []
        for i in inf:
            pibs.append(i["pib"])
        return pibs

    def add_waybill(self, pib: str, date, km):
        inf = reader("waybills.json")
        information = (pib, date, km)
        inf.append(information)
        adder(inf, "waybills.json")
        return "Маршрутний лист успішно додано!"

    def pay_for_km(self, pib, date1, date2):
        global fee_per_km, load_capacity
        date1 = date1.split("-")
        date2 = date2.split("-")
        start = date(int(date1[0]), int(date1[1]), int(date1[2]))
        end = date(int(date2[0]), int(date2[1]), int(date2[2]))
        all_waybills_of_this_man = []
        inf1 = reader("waybills.json")
        inf2 = reader("driver.json")
        for i in inf2:
            if i["pib"] == pib:
                fee_per_km = int(i["fee_per_km"])
                load_capacity = int(i["load_capacity"])
        for i in inf1:
            if i[0] == pib:
                date3 = i[1].split("-")
                date_now = date(int(date3[0]), int(date3[1]), int(date3[2]))
                if start <= date_now <= end:
                    all_waybills_of_this_man.append(i)
        pay = 0
        for i in all_waybills_of_this_man:
            pay += fee_per_km*load_capacity*int(i[2])

        return pay
