# import json


# def rewrite(name, adres):
#     with open("nice.json", "r") as f:  # json.dump(info, file, indent=3)
#         book = json.load(f)
#     with open("nice.json", "w") as f:
#         for i in book["data"]:
#             if i["first_name"] == name:
#                 i["adress"] = adres
#         json.dump(book, f, indent=3)


# rewrite("ваня", "залупкіна 46")
def pizza_seller(filename):
    all_pizzas = []
    dobavku = []
    reshta = []

    with open(filename, "r", encoding='utf-8') as f:
        for line in f.readlines():
            pizza = line.split(" ")
            # pizza.pop(-1)
            for i in pizza:
                if i == "30см":
                    all_pizzas.append(pizza)
                elif i.startswith("➕"):
                    dobavku.append(pizza)
                elif i == "1L":
                    reshta.append(pizza)
                elif i == "0.3L":
                    reshta.append(pizza)
                elif i == "0.5L":
                    reshta.append(pizza)
                    # print(1)
                    # print(reshta)
        print(all_pizzas)
        j = 0
        while j < len(all_pizzas):
            if j != len(all_pizzas) - 1:
                if all_pizzas[j][-3] >= all_pizzas[j + 1][-3]:
                    print(j)
                    num = int(all_pizzas[j + 1][-3]) / 2

                    all_pizzas[j + 1][-3] = str(num)
                else:
                    num = int(all_pizzas[j][-3]) / 2
                    all_pizzas[j][-3] = str(num)
                print(num)
                # print(all_pizzas[j][-3])
            j += 2
    # with open('nice.text', "w") as file:
    #     file.writelines()
    for i in range(len(all_pizzas)):
        all_pizzas[i] = " ".join(all_pizzas[i])
    for s in range(len(dobavku)):
        dobavku[s] = " ".join(dobavku[s])
    for d in range(len(reshta)):
        reshta[d] = " ".join(reshta[d])

    print(reshta)
    print(1)
    print(dobavku)
    print(1)
    print(all_pizzas)

    # print(all_pizzas)


pizza_seller("789402487")
