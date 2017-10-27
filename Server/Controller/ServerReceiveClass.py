import threading
from Server.Controller.ServerCommands import Commands
from Server.Controller.ServerBroadcastClass import Broadcast
from Server.View.ServerGuiFunctions import print_message_in_text_frame
from Server.View import  ServerGuiFunctions


class ReceiveServer(threading.Thread):
    def __init__(self,client_socket_,connected_clients_,chat_window_):
        threading.Thread.__init__(self)
        self.client_socket = client_socket_
        self.connected_clients = connected_clients_
        self.chat_window = chat_window_
        self.recv_size = 1024

    def run(self):
        while True:
            broadcast_to_all = Broadcast(self.client_socket,self.connected_clients,self.client_socket.recv(self.recv_size).decode())
            if broadcast_to_all.message_to_broadcast[:1] == "#":
                Commands(broadcast_to_all.message_to_broadcast)
                print("We got a command for the client")
            else:
                broadcast_to_all.start()
                print(broadcast_to_all.message_to_broadcast)
                ServerGuiFunctions.print_message_in_text_frame(broadcast_to_all.message_to_broadcast,self.chat_window)

