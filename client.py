import socket

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
client.connect(("127.0.0.1", 1234))
with open("dates.txt", "r") as file:
    text = file.readlines()

for i in range(len(text)):
    if text[i].endswith("\n"):
        text[i] = text[i].split("\n")[0]
# print(text)
data_list = []
while True:
    for i in range(len(text)):
        msg = client.send(text[i].encode("utf-8"))

    data = client.recv(2048)
    msg1 = data.decode('utf-8')
    print(msg1)
