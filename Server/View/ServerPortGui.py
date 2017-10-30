import tkinter
from Server.View.ServerGuiDesignClass import ServerGui
class Port_Window:
    def __init__(self):
        self.root1 = tkinter.Tk()
        self.port_from_input = None

    def start(self):
        key = 'abcdefghijklmnopqrstuvwxyz'
        def encrypt():

            password = password_entry.get()
            checknum = checknum_entry.get()
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

            if self.user_pass == "zkccg0bn":
                get_port()
            else:
                print("Wrong")


        def get_port():
            self.port_from_input = port_entry.get()
            print(self.port_from_input)
            self.start_gui_main()


        head_frame = tkinter.Frame(self.root1, bg="grey")
        head_frame.place()
        password_label = tkinter.Label(self.root1, text="Enter password")
        password_entry = tkinter.Entry(self.root1)
        checknum_label = tkinter.Label(self.root1, text= "Enter Checknum")
        checknum_entry = tkinter.Entry(self.root1)

        password_label.grid(row = 1, column = 0)
        password_entry.grid(row = 1, column = 1)
        checknum_label.grid(row=2, column = 0)
        checknum_entry.grid(row=2, column = 1)

        button = tkinter.Button(self.root1, text = "Login", command =encrypt)
        button.grid(row = 3, column = 0, columnspan = 2)


        port_label = tkinter.Label(self.root1, text="Input port: ")
        port_entry = tkinter.Entry(self.root1)
        port_label.grid(column=0, row=0)
        port_entry.grid(column=1, row=0)
        self.root1.mainloop()
    def start_gui_main(self):
        self.root1.destroy()
        new_gui = ServerGui(self.port_from_input)
        new_gui.start()
start = Port_Window()
start.start()
