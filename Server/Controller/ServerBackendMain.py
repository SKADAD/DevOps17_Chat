import socket

from Server.Controller.ServerReceiveClass import ReceiveServer
from Server.Controller.ServerSendClass import SendServer


class ServerBackend:
    def __init__(self, ip_, port_):
        # declare variables for the class and creating a socket and a list
        self.main_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip = ip_
        self.port = port_
        self.main_server_socket.bind((self.ip, self.port))
        self.connected_clients = []

    def start(self):
        # starting the class which make the server to start listen and wait for clients to connect.
        self.server_send()
        self.main_server_socket.listen()
        while True:
            client_socket, client_adress = self.main_server_socket.accept()
            self.connected_clients.append(client_socket)
            print("Someone connected to server")
            self.server_receive(client_socket, self.connected_clients)

    def server_send(self):
        send_to_all = SendServer(self.connected_clients)
        send_to_all.start()

    def server_receive(self, client_socket, connected_clients):

        receive_from_client = ReceiveServer(client_socket, connected_clients).start()


# trying the class
obj1 = ServerBackend('127.0.0.1', 9999)
obj1.start()
