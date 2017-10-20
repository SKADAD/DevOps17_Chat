import threading
from BroadcastClass import Broadcast

class ReceiveServer:
    def __init__(self,client_socket_,connected_clients_):
        threading.Thread.__init__(self)
        self.client_socket = client_socket_
        self.connected_clients = connected_clients_

    def run(self):
        while True:
            message_from_client = self.client_socket.recv(1024).decode()
            broadcast_to_all = Broadcast(self.client_socket,self.connected_clients,message_from_client)
            broadcast_to_all.start()