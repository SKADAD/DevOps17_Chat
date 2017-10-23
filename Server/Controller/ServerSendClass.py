import threading

class SendServer(threading.Thread):
    def __init__(self,connected_clients_):
        threading.Thread.__init__(self)
        self.connected_clients = connected_clients_

    def run(self):
        while True:
            message_to_all = input()
            for client in self.connected_clients:
                client.send(str.encode(message_to_all))
            print(message_to_all)