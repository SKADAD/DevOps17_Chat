import socket
import threading
import time
import pickle
from Server.Controller.ServerReceiveClass import ReceiveServer
from Server.Controller.ServerSendClass import SendServer
from Server.Model.UserClass import User


class ServerBackend(threading.Thread):
    def __init__(self, ip_, port_,chat_window_):
        threading.Thread.__init__(self)
        # declare variables for the class and creating a socket and a list
        self.main_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip = ip_
        self.port = port_
        self.chat_window = chat_window_
        self.main_server_socket.bind((self.ip, self.port))
        self.connected_clients = []
        self.client_socket = None
        self.client_adress = None
        self.registered_users = []
        self.clients_online=[]

    def run(self):
        self.unpickle_user_account()
        # starting the class which make the server to start listen and wait for clients to connect.
        self.main_server_socket.listen()
        users_online = threading.Thread(target=self.update_connected_users,).start()

        while True:
            self.client_socket, self.client_adress = self.main_server_socket.accept()
            #self.connected_clients.append(self.client_socket)
            print("Someone connected to server")
            login_worker = threading.Thread(target=self.log_in_register, args=(self.client_socket, self.connected_clients, self.chat_window))
            login_worker.start()

    def server_send(self, message):
        SendServer(self.connected_clients, message).start()

    def log_in_register(self, client_socket, connected_clients, chat_window):
        while True:
            login_or_register = client_socket.recv(1024).decode()
            print(login_or_register)
            credentials = login_or_register[1:].split()
            print(credentials)
            if login_or_register[0] == '1':
                result = self.client_log_in(credentials[0], credentials[1])

                if result == 'correct':
                    client_socket.send(str.encode('correct'))
                    time.sleep(0.5)
                    break

                elif result == 'wrong password':
                    client_socket.send(str.encode('wrong password'))
                    time.sleep(0.5)
                    continue

                elif result == 'no account':
                    client_socket.send(str.encode('no account'))
                    time.sleep(0.5)
                    continue


            elif login_or_register[0] == '2':
                result = self.create_user_account(credentials[0], credentials[1], credentials[2])

                if result == 'account exists':
                    client_socket.send(str.encode('account exists'))
                    time.sleep(0.5)
                    continue

                elif result == 'nickname exists':
                    client_socket.send(str.encode('nickname exists'))
                    time.sleep(0.5)
                    continue

                elif result == 'account created':
                    client_socket.send(str.encode('account created'))
                    time.sleep(0.5)
                    break
            else:
                print('Ogiltigt')
                break

        self.server_receive(client_socket, connected_clients, chat_window, credentials[2])
        self.connected_clients.append(self.client_socket)
        self.clients_online.append(credentials[2])
        self.update_connected_users()



    def server_receive(self, client_socket, connected_clients, chat_window, client_name,):
        ReceiveServer(client_socket, connected_clients, chat_window, client_name,self.clients_online).start()


    def create_user_account(self, account_name, password, nickname):
        new_user = User(account_name, password, nickname)
        for user in self.registered_users:
            if new_user.account_name == user.account_name:
                return 'account exists'
        for nickname in self.registered_users:
            if new_user.nickname == nickname.nickname:
                return 'nickname exists'
        self.registered_users.append(new_user)
        self.pickle_user_account()
        return 'account created'


    def client_log_in(self, entered_account_name, entered_password):
        index = -1
        for i in range(len(self.registered_users)):
            if self.registered_users[i].account_name == entered_account_name:
                index = i
                break

        if index != -1:
            if self.registered_users[index].password == entered_password:
                return 'correct'
            else:
                return 'wrong password'
        else:
            return 'no account'

    def update_connected_users(self):
            online = "#connected"

            for client in self.clients_online:
                online += " " + client

            self.server_send(online)
            print(online)

    def unpickle_user_account(self):
        pickle_in = open("user_pickle.pickle", 'rb')
        try:
            while True:
                self.registered_users.append(pickle.load(pickle_in))
        except EOFError:
            pass
        pickle_in.close()

    def pickle_user_account(self):
        pickle_out = open("user_pickle.pickle", 'wb')
        for user in range(len(self.registered_users)):
            pickle.dump(self.registered_users[user], pickle_out)
        pickle_out.close()









                # def client_log_out(self, name):
    #     self.clients_online.remove(name)

        # for client in self.clients_online:
        #     if self.clients_online[client]==name:
        #         self.clients_online.pop(client)


