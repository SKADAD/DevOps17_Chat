import tkinter
import time
import tkinter.messagebox
from Server.View import ServerGuiFunctions
#import ServerGuiFunctions



class ServerGui:

    def __init__(self, clients_ip_, clients_port_, user_name_):
        self.clients_ip = clients_ip_
        self.clients_port = clients_port_
        self.user_name = user_name_

        self.root = tkinter.Tk()

        self.root.title('GONE CHAT')
        self.root.iconbitmap(default='../../images/ikon.ico')
        self.root.configure(bg='white')
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

        self.input_window = tkinter.Text(self.chat_entry_frame, width=50, height=3, borderwidth=2, wrap=tkinter.WORD,relief='ridge')


        self.logo_frame.place(x = 20, y = 30, width = 300, height = 70)
        self.chat_frame.place(x = 20, y = 110, width = 700, height = 400)
        self.chat_entry_frame.place(x = 20, y = 530, width = 600, height = 90)
        #self.send_button.place(x = 630, y = 530, width = 90, height = 90)
        self.server_info.place(x = 630, y = 30, width = 300, height = 70)
        self.server_list.place(x = 730, y = 110, width = 200, height = 510)



    def start(self):
        #Function to start
        self.logo_create()
        self.chat_input_frame()
        self.chat_button_create()

        self.root.mainloop()




    def logo_create(self):
        logo_image = tkinter.PhotoImage(file = '../../images/Gone_Logo.png')
        logo_label = tkinter.Label(self.root, image = logo_image, border = 0)
        logo_label.image = logo_image
        logo_label.place(x = 20, y = 30, width = 300, height = 70)

    def chat_button_create(self):
        self.send_image = tkinter.PhotoImage(file='../../images/button_send.png')
        self.send_button = tkinter.Button(self.root, image=self.send_image, command = lambda: self.test_print()) #Glöm ej ändra funktion
        self.send_button.image = self.send_image
        self.send_button.place(x=630, y=530, width=90, height=90)



    def chat_frame_create(self):
        self.chat_frame.place(x=20, y=110, width=700, height=400)
        self.chat_frame.see('end')
        self.chat_frame.configure(state="disabled")

    def chat_input_frame(self):
        def get_message_from_input_window():
            message = self.chat_input_frame().get("1.0", 'end-1c')
            if message.isspace() or len(message) == 0:
                self.chat_input_frame().delete('1.0', 'end')
            else:
                ServerGuiFunctions.print_message_in_text_frame(message, self.chat_frame_create())
                self.input_window.delete('1.0', 'end')


#############
    def test_print(self):
        print("Hello, world")
#############




test = ServerGui('16', '16', 'Kim')
test.start()