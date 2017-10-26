import socket
import threading
from Server.Controller.ServerReceiveClass import ReceiveServer
from Server.Controller.ServerSendClass import SendServer



class ServerBackend(threading.Thread):
    def __init__(self, ip_, port_,gui_root_):
        threading.Thread.__init__(self)
        # declare variables for the class and creating a socket and a list
        self.main_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip = ip_
        self.port = port_
        self.gui_root = gui_root_
        self.main_server_socket.bind((self.ip, self.port))
        self.connected_clients = []


    def run(self):
        # starting the class which make the server to start listen and wait for clients to connect.
        self.main_server_socket.listen()
        while True:
            client_socket, client_adress = self.main_server_socket.accept()
            self.connected_clients.append(client_socket)
            print("Someone connected to server")
            self.server_receive(client_socket, self.connected_clients, self.gui_root)

    def server_send(self,message):
        SendServer(self.connected_clients,message).start()

    def server_receive(self, client_socket, connected_clients, gui_root_):
        ReceiveServer(client_socket, connected_clients, gui_root_).start()


# trying the class
#obj1 = ServerBackend('172.20.201.234', 9999)
#obj1.start()
