import threading

class Sender(threading.Thread):
    def __init__(self,server_socket_,message_to_send_):
        threading.Thread.__init__(self)
        self.server_socket=server_socket_
        self.message=message_to_send_

    def run(self):
        self.message = input()
        self.server_socket.send(str.encode(self.message))

print("Hello")