import threading



class Receiver(threading.Thread):
    def __init__(self,server_socket_):
        threading.Thread.__init__(self)
        self.server_socket=server_socket_
        self.recv_size=1024

    def run(self):
        while True:
            message_from_server=self.server_socket.recv(self.recv_size)
            print(message_from_server)

print("heelo")