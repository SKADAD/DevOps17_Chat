from Client.View.ClientGuiDesignClass import ClientGui

class Commands:
    def __init__(self,message_from_server_):
        self.message=message_from_server_


    def commands(self):

        #Update users online OBS O TESTAT!!
        if self.message[:9]== "connected":
            print("Här updaterar vi listan med connected users")
            connectedusers=self.message[9:]
            connectedusers.split()
            self.list_of_active_users=[]
            for i in connectedusers:
                self.list_of_active_users.append(i)





