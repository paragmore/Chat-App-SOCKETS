from socket import AF_INET, socket, SOCK_STREAM
from threading import  Thread

HOST = 'localhost'
PORT = 5000
BUFFSIZE = 1024
ADDR =(HOST,PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)