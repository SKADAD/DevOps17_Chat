#from Client.View.ClientGuiDesignClass import ClientGui

class Commands:
    def __init__(self,message_from_server_,active_users_list_):
        self.message=message_from_server_
        self.active_users_list = active_users_list_


    def connected_users(self):

        #Update users online OBS O TESTAT!!
        print("Här updaterar vi listan med connected users")
        self.active_users_list.delete(0,'end')
        connectedusers=self.message[9:]
        splitedconnected=connectedusers.split()
        list_of_active_users=[]
        for user in splitedconnected:
            self.active_users_list.insert('end', user)
            # self.active_users_list.append("'"+i+"'")
            # print("appendar "+(i))


        print("Vi kom hit men inget hönder :D")




