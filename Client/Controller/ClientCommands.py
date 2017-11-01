#from Client.View.ClientGuiDesignClass import ClientGui

class Commands:
    def __init__(self,message_from_server_,active_users_list_):
        self.message=message_from_server_
        self.active_users_list = active_users_list_


    def connected_users(self):

        self.active_users_list.delete(0,'end')
        connectedusers=self.message[9:]
        splitedconnected=connectedusers.split()
        for user in splitedconnected:
            self.active_users_list.insert('end', user)




