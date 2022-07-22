import os

for root, dirs, files in os.walk(r'C:\Users\icaev\PycharmProjects\ira_labku'):
    for file in files:
        if os.stat(rf'C:\Users\icaev\PycharmProjects\ira_labku\{file}').st_size >= 1024.0:
            # filename.upload_file(os.path.join(root, file), BUCKET_NAME, file)
            print(file.split(".")[0])
            print(os.stat(rf'C:\Users\icaev\PycharmProjects\ira_labku\{file}').st_size)
        # else:
            # print("no files found")
print("data available")
