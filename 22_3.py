import os

rootPath = r"C:\Users\icaev\PycharmProjects\ira_labku"
all_ = [[], []]
all_files = []
for root, dir_name, filename in os.walk(rootPath):
    all_[0].append(root)
    all_[1].append(dir_name)
    for i in filename:
        all_files.append(i)
fw = []
cout = 0
count = 0
for j in all_files:
    for i in all_files:
        if j == i:
            try:

                file_weight = os.stat(f"{all_[0][count+1]}\\{j}").st_size - os.stat(f"{all_[0][cout-1]}\\{i}").st_size
                print(file_weight)
                fw.append(str(file_weight) + "\n")
            except Exception as e:
                continue
        cout += 1
    count += 1
