import threading
from ServerBroadcastClass import Broadcast

class ReceiveServer(threading.Thread):
    def __init__(self,client_socket_,connected_clients_):
        threading.Thread.__init__(self)
        self.client_socket = client_socket_
        self.connected_clients = connected_clients_
        self.recv_size = 1024

    def run(self):
        while True:
            broadcast_to_all = Broadcast(self.client_socket,self.connected_clients,self.client_socket.recv(self.recv_size).decode())
            broadcast_to_all.start()
            print(broadcast_to_all.message_to_broadcast)