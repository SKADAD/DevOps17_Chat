class Commands:
    def __init__(self,message_from_server_):
        self.message=message_from_server_


    def commands(self):

        #Update
        if self.message[:9]== "connected":
            print("Här updaterar vi listan med connected users")
            connectedusers=self.message[9:]



