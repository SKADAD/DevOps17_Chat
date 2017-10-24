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

        self.root.title('GONE CHAT - SERVER')
        self.root.iconbitmap(default='../../images/ikon.ico')
        self.root.configure(bg='ivory2')
        # width x height + x offset + y offset:
        self.root.geometry("1200x700+30+30")
        self.root.minsize(width = 1200, height = 700)

        #Gui framwork
        self.logo_frame = tkinter.Frame(self.root, highlightbackground = 'black', highlightthickness= 2)
        self.chat_window = tkinter.Frame(self.root, bg='wheat3', highlightbackground = 'black', highlightthickness= 2)
        self.chat_entry_frame = tkinter.Frame(self.root, bg='bisque2', highlightbackground = 'black', highlightthickness= 2)
        self.send_button = tkinter.Frame(self.root, bg='ivory2', highlightbackground='black', highlightthickness=2)
        self.server_info = tkinter.Frame(self.root, bg='gray18', highlightbackground='black', highlightthickness=2)
        self.server_list = tkinter.Frame(self.root, bg='bisque2', highlightbackground='black', highlightthickness=2)



        self.logo_frame.place(x = 20, y = 30, width = 300, height = 70)
        self.chat_window.place(x = 20, y = 110, width = 700, height = 400)
        #self.chat_entry_frame.place(x = 20, y = 530, width = 600, height = 90)
        #self.send_button.place(x = 630, y = 530, width = 90, height = 90)
        self.server_info.place(x = 630, y = 30, width = 300, height = 70)
        self.server_list.place(x = 730, y = 110, width = 200, height = 510)

        # Text widgets created
        self.chat_window = tkinter.Text(self.chat_window, wrap=tkinter.WORD)
        self.send_message_frame = tkinter.Frame(self.chat_entry_frame)
        self.input_window = tkinter.Text(self.root, width=50, height=3, borderwidth=2, wrap=tkinter.WORD)


    def start(self):

        self.logo_create()
        self.chat_input_frame()
        self.chat_frame_create()
        #self.server_info()

        self.root.mainloop()
    '''
    def server_info(self):
        server_uptime = 0
        server_runtime = tkinter.Text(self.root)
        server_runtime.insert('insert', server_uptime)
        server_runtime.place(x=650, y=50)

        while True:
            server_runtime.delete('1.0', 'end')
            server_uptime = server_uptime + 1
            time.sleep(1)
            server_runtime.insert('insert', server_uptime)
    '''

    def logo_create(self):
        logo_image = tkinter.PhotoImage(file = '../../images/Gone_Logo.png')
        logo_label = tkinter.Label(self.root, image = logo_image, border = 0)
        logo_label.image = logo_image
        logo_label.place(x = 20, y = 30, width = 300, height = 70)




    def chat_frame_create(self):
        self.chat_window.place(x = 0, y = 0, width = 695, height = 395)
        self.chat_window.see('end')
        self.chat_window.configure(state="disabled")



    def chat_input_frame(self):

        def get_message_from_input_window():
            message = self.input_window.get("1.0", 'end-1c')
            if message.isspace() or len(message) == 0:
                self.input_window.delete('1.0', 'end')
            else:
                ServerGuiFunctions.print_message_in_text_frame(message, self.chat_window)
                self.input_window.delete('1.0', 'end')

        def send_with_enter(event):
            get_message_from_input_window()
            return 'break'

        def new_line(event):
            self.input_window.insert('insert', '{}'.format(''))

        self.chat_entry_frame.place(x=20, y=530, width=600, height=90)
        self.input_window.bind('<Return>', send_with_enter)
        self.input_window.bind('<Shift-Return>', new_line)

        self.input_window.place(x=20, y=530, width=600, height=90)

        send_image = tkinter.PhotoImage(file='../../images/button_send.png')
        send_button = tkinter.Button(self.root, image=send_image, command = get_message_from_input_window) #Glöm ej ändra funktion
        send_button.image = send_image
        send_button.place(x=630, y=530, width=90, height=90)

#############
    def test_print(self):
        print("Hello, world")
#############



test = ServerGui('16', '16', 'Kim')
test.start()