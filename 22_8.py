import os
import json


rootPath = r"C:\Users\icaev\PycharmProjects\ira_labku\f1"
file_info = {"data": []}
new_file_or_dir_info = {"filename": "",
                        "last_open": "",
                        "file_size": ""}
for root, path_name, filename in os.walk(rootPath):
    for file in filename:
        size = os.stat(f"{root}\\{file}").st_size
        last_open = os.stat(f"{root}\\{file}").st_mtime
        new_file_or_dir_info["filename"] = file
        new_file_or_dir_info["last_open"] = last_open
        new_file_or_dir_info["file_size"] = size
        file_info["data"].append(new_file_or_dir_info)
    for path in path_name:
        size = os.stat(f"{root}\\{path}").st_size
        last_open = os.stat(f"{root}\\{path}").st_mtime
        new_file_or_dir_info["filename"] = path
        new_file_or_dir_info["last_open"] = last_open
        new_file_or_dir_info["file_size"] = size
        file_info["data"].append(new_file_or_dir_info)

with open("out.json", 'w') as file:
    json.dump(file_info, file, indent=3)
