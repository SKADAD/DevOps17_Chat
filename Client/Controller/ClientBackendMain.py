import socket
import threading
from Client.Controller.ClientReceiveClass import Receiver
from Client.Controller.ClientSendClass import Sender
from Client.Controller.ClientCommands import Commands
import time

class ClientBackend(threading.Thread):

    def __init__(self,server_ip_,server_port_,chat_window_,active_users_list_,):
        threading.Thread.__init__(self)
        self.server_ip=server_ip_
        self.server_port=server_port_
        self.chat_window = chat_window_
        self.active_users_list=active_users_list_
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    def start (self):

        #Connect to server
        self.client.connect((str(self.server_ip),int(self.server_port)))
        print("Connection established")


    def start_reciever(self):
        # Starting new thread to recive messages from server
        receiver = Receiver(self.client, self.chat_window, self.active_users_list).start()

    def server_send(self, message):

        Sender(self.client, message).start()
    print("Connection established")



##Test objekt till klassen ska bort i finalrelease.
#
# test=ClientBackend('127.0.0.1',9999,"")
# test.start()
