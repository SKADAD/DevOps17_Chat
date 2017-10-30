import socket
import threading
from Server.Controller.ServerReceiveClass import ReceiveServer
from Server.Controller.ServerSendClass import SendServer


class ServerBackend(threading.Thread):
    def __init__(self, ip_, port_,chat_window_):
        threading.Thread.__init__(self)
        # declare variables for the class and creating a socket and a list
        self.main_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip = ip_
        self.port = port_
        self.chat_window = chat_window_
        self.main_server_socket.bind((self.ip, self.port))
        self.connected_clients = []
        self.client_socket = None
        self.client_adress = None

    def run(self):
        # starting the class which make the server to start listen and wait for clients to connect.
        self.main_server_socket.listen()
        while True:
            self.client_socket, self.client_adress = self.main_server_socket.accept()
            self.connected_clients.append(self.client_socket)
            print("Someone connected to server")
            self.server_receive(self.client_socket, self.connected_clients, self.chat_window)

    def server_send(self, message):
        SendServer(self.connected_clients, message).start()

    def server_receive(self, client_socket, connected_clients, chat_window):
        ReceiveServer(client_socket, connected_clients, chat_window).start()
