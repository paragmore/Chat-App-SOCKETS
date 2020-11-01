from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from chatter import Chatter

HOST = 'localhost'
PORT = 5000
ADDR = (HOST, PORT)
MAX_CONNECTIONS= 5
BUFFSIZE = 1024 # size of messages

chatters = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def broadcast(msg, name):
    """send messages"""
    for chatter in chatters:
        client = chatter.client
        client.send(bytes(name + ": ", "utf8"), msg)


def client_communication(chatter):
    """handles client messages"""
    client = chatter.client

    name = client.recv(BUFFSIZE).decode("utf8")
    msg = f"{name} has joined the chat."
    broadcast(msg)

    while True:
        try:
            msg = client.recv(BUFFSIZE)
            print(f"{name} : ", msg.decode("utf8"))
            if msg == bytes("{quit}", "utf8"):
                broadcast(f"{name} has left the chat...", "")
                client.send(bytes("{quit}", "utf8"))
                client.close()
                chatters.remove(chatter)
                break
            else:
                broadcast(msg, name)
        except Exception as e:
            print("[EXCEPTION]: ",e)
            break

def wait_for_connection():
    """wait for client connecting and after successful connection start new client communication thread"""
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            chatter = Chatter(addr,client)
            chatters.append(chatter)
            print(f"[CONNECTION]{addr} connected to server at {time.time()}")
            Thread(target=client_communication, args=(chatter,).start())
        except Exception as e:
            print("[EXCEPTION]: ",e)
            run = False
    print("SERVER CRASH")


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS)
    print("[STARTED] Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection,)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()