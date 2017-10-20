import threading

class Broadcast:
    def __init__(self,client_socket_,connected_clients_,message_from_client_):
        threading.Thread.__init__(self)
        self.client_socket = client_socket_
        self.connected_clients = connected_clients_
        self.message_to_broadcast = message_from_client_

    def Run(self):
        while True:
            message_to_broadcast = self.message_to_broadcast
            for client in self.connected_clients:
                client.send(str.encode(message_to_broadcast))