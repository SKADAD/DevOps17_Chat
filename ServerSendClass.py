import threading

class SendServer(threading.Thread):
    def __init__(self,client_socket_):
        threading.Thread.__init__(self)
        self.client_socket = client_socket_
        self.message_to_all = input("Skriv något till alla: ")

    def run(self):
        while True:
            message_from_server = self.message_to_all
            for client in self.client_socket:
                client.send(str.encode("Message from server "+message_from_server))