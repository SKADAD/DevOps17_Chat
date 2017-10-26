import threading
from Client.Controller.ClientCommands import Commands
from Client.View import ClientGuiFunctions


class Receiver(threading.Thread):
    def __init__(self,client_socket_,chat_window_):
        threading.Thread.__init__(self)
        self.client_socket=client_socket_
        self.chat_window=chat_window_
        self.recv_size=1024

    def run(self):
        while True:
            message_from_server=self.client_socket.recv(self.recv_size).decode()

            if message_from_server[:1] =="#":
                # Commands from server in form of #
                message=message_from_server[1:]
                Commands(message)
                print ("We got an server command!")

            else:
                print("Message from server: " + message_from_server)
                ClientGuiFunctions.print_message_in_text_frame(message_from_server, self.chat_window)

