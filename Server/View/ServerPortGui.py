import tkinter
import socket
import tkinter.messagebox
from Server.View.ServerGuiDesignClass import ServerGui
class Port_Window:
    def __init__(self):
        self.root1 = tkinter.Tk()
        self.root1.title('Port/Login')
        self.root1.iconbitmap('../../images/ikon.ico')
        self.port_from_input = None
        self.root1.geometry("225x90")
        self.root1.resizable(0,0)

    def start(self):
        key = 'abcdefghijklmnopqrstuvwdxyz'
        def encrypt():

            password = password_entry.get()
            checknum = checknum_entry.get()
            check_port = port_entry.get()


            if (len(password)==0 or len(checknum) == 0 or len(check_port) == 0)or(password.isspace()or checknum.isspace()or check_port.isspace()):
                tkinter.messagebox.showwarning(title='Error', message='Cant leave fields empty.')
                return
            else:
                int_checknum = int(checknum)
                result = ""
                for l in password.lower():
                    try:
                        i = (key.index(l) + int_checknum) % 26
                        result += key[i]
                    except ValueError:
                        result += l

                print(result.lower())
                self.user_pass = result.lower()

                if self.user_pass == "ykccgxbn":
                    get_port()
                else:
                    tkinter.messagebox.showwarning(title='Error',message='Wrong password')


        def get_port():
            self.port_from_input = port_entry.get()
            port_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                port_socket.bind(('', int(self.port_from_input)))
                port_socket.close()
                self.start_gui_main()
            except:
                tkinter.messagebox.showwarning(title='Error', message='Port is already taken')

        head_frame = tkinter.Frame(self.root1, bg="grey")
        head_frame.place()
        password_label = tkinter.Label(self.root1, text="Enter password",font=('calibri', 10))
        password_entry = tkinter.Entry(self.root1, bg='lightgray')
        checknum_label = tkinter.Label(self.root1, text= "Enter Checknum",font=('calibri', 10))
        checknum_entry = tkinter.Entry(self.root1, bg='lightgray')

        password_label.grid(row = 1, column = 0)
        password_entry.grid(row = 1, column = 1)
        checknum_label.grid(row=2, column = 0)
        checknum_entry.grid(row=2, column = 1)

        button = tkinter.Button(self.root1, text = "Start server", command =encrypt)
        button.grid(row = 3, column = 0, columnspan = 2)


        port_label = tkinter.Label(self.root1, text="Input port: ",font=('calibri', 10))
        port_entry = tkinter.Entry(self.root1,bg='lightgray')
        port_label.grid(column=0, row=0)
        port_entry.grid(column=1, row=0)
        self.root1.mainloop()
    def start_gui_main(self):
        self.root1.destroy()
        new_gui = ServerGui(self.port_from_input)
        new_gui.start()
start = Port_Window()
start.start()
