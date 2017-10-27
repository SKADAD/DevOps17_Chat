import tkinter
from Server.View.ServerGuiDesignClass import ServerGui
class Port_Window:
    def __init__(self):
        self.root1 = tkinter.Tk()
        self.port_from_input = None

    def start(self):
        def get_port():
            self.port_from_input = port_entry.get()
            print(self.port_from_input)
            self.start_gui_main()

        self.root1.geometry("250x50+10+10")

        head_frame = tkinter.Frame(self.root1, bg="grey")
        head_frame.place()

        port_label = tkinter.Label(self.root1, text="Input port: ")
        port_entry = tkinter.Entry(self.root1)
        port_button = tkinter.Button(self.root1, text="Enter", command=get_port)
        port_label.grid(column=0, row=0)
        port_entry.grid(column=1, row=0)
        port_button.grid(column=2, row=0)
        self.root1.mainloop()
    def start_gui_main(self):
        self.root1.destroy()
        new_gui = ServerGui(self.port_from_input)
        new_gui.start()
start = Port_Window()
start.start()