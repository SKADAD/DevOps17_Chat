import socket
from Client.Controller.ClientReceiveClass import Receiver
from Client.Controller.ClientSendClass import Sender

class ClientBackend:

    def __init__(self,server_ip_,server_port_,username_):
        self.server_ip=server_ip_
        self.server_port=server_port_
        self.username=username_
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    def start (self):

        #Connect to server
        self.client.connect((self.server_ip,self.server_port))

        #Starting new thread to recive messages from server
        receiver = Receiver(self.client).start()


        # Starting new thread to send messages to server
        sender = Sender(self.client,"TA BORT DETTA SEN!!").start()
        print("Connection established")

