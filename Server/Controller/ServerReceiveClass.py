import threading
from Server.Controller.ServerCommands import Commands
from Server.Controller.ServerBroadcastClass import Broadcast
from Server.Controller.ServerSendClass import SendServer
from Server.View import ServerGuiFunctions



class ReceiveServer(threading.Thread):
    def __init__(self  , client_socket_, connected_clients_, chat_window_, client_name_, clients_online_):
        threading.Thread.__init__(self)
        self.client_socket = client_socket_
        self.connected_clients = connected_clients_
        self.chat_window = chat_window_
        self.recv_size = 1024
        self.client_name=client_name_
        self.clients_online=clients_online_

    def run(self):
        try:
            while True:
                broadcast_to_all = Broadcast(self.client_socket,self.connected_clients,self.client_name+": "+self.client_socket.recv(self.recv_size).decode())
                if broadcast_to_all.message_to_broadcast[:1] == "#":
                    Commands(broadcast_to_all.message_to_broadcast)
                    print("We got a command for the client")
                else:
                    broadcast_to_all.start()
                    print(broadcast_to_all.message_to_broadcast)
                    ServerGuiFunctions.print_message_in_text_frame(broadcast_to_all.message_to_broadcast,self.chat_window)
        except:
            self.connected_clients.remove(self.client_socket)
            self.client_socket.close()
            msg="Server message: "+self.client_name+" has disconnected!"
            self.clients_online.remove(self.client_name)
            SendServer(self.connected_clients,msg).start()
            self.update_connected_users()

    def update_connected_users(self):
        online = "#connected"

        for i in range(len(self.clients_online)):
            online += " " + self.clients_online[i]

        SendServer(self.connected_clients, online).start()
        print(online)

