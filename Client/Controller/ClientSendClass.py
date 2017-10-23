import threading


class Sender(threading.Thread):
    def __init__(self,client_socket_,message_to_send_):
        threading.Thread.__init__(self)
        self.client_socket=client_socket_
        self.message=message_to_send_

    def run(self):
        while True:
            self.message = input()
            self.client_socket.send(str.encode(self.message))

