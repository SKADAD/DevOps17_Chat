import threading

class SendServer(threading.Thread):
    def __init__(self,connected_clients_,message_to_all_):
        threading.Thread.__init__(self)
        self.connected_clients = connected_clients_
        self.message_to_all = message_to_all_

    def run(self):
        for client in self.connected_clients:
             client.send(str.encode(self.message_to_all))
        print(self.message_to_all)
