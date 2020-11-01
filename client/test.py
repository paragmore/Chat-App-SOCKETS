from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


HOST = 'localhost'
PORT = 5000
ADDR = (HOST, PORT)
BUFFSIZE = 1024

messages = []

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


def receive_messages():
    while True:
        try:
            msg = client_socket.recv(BUFFSIZE).decode("utf8")
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("[EXCEPTION]: ", e)
            break


def send_message(msg):
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()


receive_thread = Thread(target=receive_messages)
receive_thread.start()

send_message("Parag")
send_message("hello")
send_message("Parag")
send_message("hello")
send_message("Parag")
send_message("hello")