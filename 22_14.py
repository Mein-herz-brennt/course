import os

filenames = os.listdir(os.getcwd())

dict_of_razni = {}

for i in range(len(filenames)):
    list_of_odnakovi = []
    for j in range(len(filenames)):
        if filenames[i].split(".")[1] == filenames[j].split(".")[1]:
            list_of_odnakovi.append(filenames[j])
    dict_of_razni[filenames[i].split(".")[1]] = list_of_odnakovi

list_of_string = []

for key, item in dict_of_razni:
    list_of_weights = []

    for it in item:
        weight = os.stat(it).st_size
        list_of_weights.append(weight)
    string = f"розширення: {key}, кількість файлів: {len(item)}, розмір кожного з файлів в байтах: {list_of_weights}\n"
    list_of_string.append(string)

with open("out.txt", "w") as file:
    file.writelines(list_of_string)
