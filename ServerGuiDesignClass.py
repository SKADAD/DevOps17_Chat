import tkinter
import tkinter.messagebox
#import ServerGuiFunctions


class ServerGui:

    def __init__(self, clients_ip_, clients_port_):
        self.clients_ip = clients_ip_
        self.clients_port = clients_port_


        self.root = tkinter.Tk()
        self.root.configure(bg = 'white')
        # width x height + x offset + y offset:
        self.root.geometry("1200x700+30+30")
        self.root.minsize(width = 1200, height = 700)


#################################################################3

        #Gui framwork
        self.logo_frame = tkinter.Frame(self.root, highlightbackground = 'black', highlightthickness= 2)
        self.chat_frame = tkinter.Frame(self.root, bg='white', highlightbackground = 'black', highlightthickness= 2)
        self.chat_entry_frame = tkinter.Frame(self.root, bg='white', highlightbackground = 'black', highlightthickness= 2)
        self.send_button = tkinter.Frame(self.root, bg='white', highlightbackground='black', highlightthickness=2)
        self.server_info = tkinter.Frame(self.root, bg='white', highlightbackground='black', highlightthickness=2)
        self.server_list = tkinter.Frame(self.root, bg='white', highlightbackground='black', highlightthickness=2)

        self.logo_frame.place(x = 20, y = 30, width = 300, height = 70)
        self.chat_frame.place(x = 20, y = 110, width = 700, height = 400)
        self.chat_entry_frame.place(x = 20, y = 530, width = 600, height = 90)
        self.send_button.place(x = 630, y = 530, width = 90, height = 90)
        self.server_info.place(x = 630, y = 30, width = 300, height = 70)
        self.server_list.place(x = 730, y = 110, width = 200, height = 510)

    def start(self):
        #Function to start

        self.send_button_create()
        self.logo_create()
        self.root.mainloop()


    def send_button_create(self):
        button_image = tkinter.PhotoImage(file ='images/SendButton.png/')
        button_label = tkinter.Label(self.root, image = button_image, border = 0)
        button_label.image = button_image
        button_label.place(x=630, y=530, width=90, height=90)

    def logo_create(self):
        logo_image = tkinter.PhotoImage(file = 'images/Gone_Logo.png/')
        logo_label = tkinter.Label(self.root, image = logo_image, border = 0)
        logo_label.image = logo_image
        logo_label.place(x = 20, y = 30, width = 300, height = 70)


    #def create_base_frames(self):



#####################################################

    #def frame(self):



test = ServerGui('16', '16')
test.start()