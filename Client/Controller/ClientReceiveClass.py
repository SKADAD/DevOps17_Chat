import threading
from Client.Controller.ClientCommands import Commands


class Receiver(threading.Thread):
    def __init__(self,client_socket_):
        threading.Thread.__init__(self)
        self.client_socket=client_socket_
        self.recv_size=1024

    def run(self):
        while True:
            message_from_server=self.client_socket.recv(self.recv_size).decode()

            if message_from_server[:1] =="#":
                message=message_from_server[1:]
                Commands(message)
                print ("We got an server command!")

            else:
                print("Message from server: " + message_from_server)

