import socket
from ClientReceiveClass import Receiver
from ClientSendClass import Sender

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',9999))
receiver = Receiver(client).start()


message_to_send=input("Skriv något till server")
sender = Sender(client,message_to_send).start()

print("hello")