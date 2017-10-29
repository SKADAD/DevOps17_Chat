import tkinter
from Server.View.ServerPortGui import Port_Window

class Login:

    def __init__(self):
        self.password_and_checknum = tkinter.Tk()

    def gui(self):
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
                self.server_login()
            else:
                print("Wrong")

            self.server_login()

        password_label = tkinter.Label(self.password_and_checknum, text = "Enter password")
        password_entry = tkinter.Entry(self.password_and_checknum)

        checknum_label = tkinter.Label(self.password_and_checknum, text= "Enter Checknum")
        checknum_entry = tkinter.Entry(self.password_and_checknum)

        password_label.grid(row = 1, column = 0)
        password_entry.grid(row = 1, column = 1)
        checknum_label.grid(row=2, column = 0)
        checknum_entry.grid(row=2, column = 1)

        button = tkinter.Button(self.password_and_checknum, text = "Login", command =encrypt)
        button.grid(row = 3, column = 0, columnspan = 2)

        self.password_and_checknum.mainloop()

    def server_login(self):
        self.password_and_checknum.destroy()
        Server_start = Port_Window()
        Server_start.start()



L=Login()
L.gui()

