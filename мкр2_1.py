import os
import re


def obednahhya(directory):  # повний шлях до директорії
    filenames_ = []
    filenames = os.listdir(directory)
    for files in filenames:
        files.split(".")
        if re.match(r"\d{3}", files[0]).end():
            filenames_.append(files[0])
    text = []
    for i in range(len(filenames_)):
        with open(f"{filenames_[i]}.text") as file:
            text += file.readlines()

    with open("all_text_from_files.txt", "w") as file:
        file.writelines(text)
    return 1
