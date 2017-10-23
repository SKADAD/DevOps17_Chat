import threading

class Broadcast(threading.Thread):
    def __init__(self,client_socket_,connected_clients_,message_from_client_):
        threading.Thread.__init__(self)
        self.client_socket = client_socket_
        self.connected_clients = connected_clients_
        self.message_to_broadcast = message_from_client_

    def run(self):
         for client in self.connected_clients:
            client.send(str.encode(self.message_to_broadcast))