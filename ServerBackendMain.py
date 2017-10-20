import socket
from ReceiveServerClass import ReceiveServer
from SendServerClass import SendServer

main_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

main_server_socket.bind = (('',9999))
main_server_socket.listen()

connected_clients = []
message = input
send_to_all = SendServer(connected_clients,message)
send_to_all.start()

while True:
    client_socket, client_adress = main_server_socket.accept()
    connected_clients.append(client_socket)
    print("Someone connected to server")
    receive_from_client = ReceiveServer(client_socket,connected_clients)
    receive_from_client.start()