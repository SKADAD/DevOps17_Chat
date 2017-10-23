import socket

from Client.Controller.ClientReceiveClass import Receiver
from Client.Controller.ClientSendClass import Sender

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',9999))
receiver = Receiver(client).start()


message_to_send=input("Skriv något till server")
sender = Sender(client,message_to_send).start()

print("hello")