import threading

class SendServer:
    def __init__(self,client_socket_,message_to_all_):
        threading.Thread.__init__(self)
        self.client_socket = client_socket_
        self.message_to_all = message_to_all_
    def Run(self):
        while True:
            message_from_server = self.message_to_all
            self.client_socket.send(str.encode(message_from_server))