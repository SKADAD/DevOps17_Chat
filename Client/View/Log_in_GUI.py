import tkinter
import time

from Client.View.ClientGuiDesignClass import ClientGui

class Login:

	def __init__(self):
		self.choose_ip_and_port_root = tkinter.Tk()
		self.ip = None
		self.port = None

	def start(self):
		def sub_func_set_ip_and_port():
			ip_get = ip_entry.get()
			port_get = port_entry.get()

			self.ip = ip_get
			self.port = int(port_get)

		top_label = tkinter.Label(self.choose_ip_and_port_root, text='Enter IP and Port of Server')
		top_label.grid(row=0, column=0, columnspan=2)

		ip_label = tkinter.Label(self.choose_ip_and_port_root, text='IP: ')
		ip_entry = tkinter.Entry(self.choose_ip_and_port_root)

		port_label = tkinter.Label(self.choose_ip_and_port_root, text='Port: ')
		port_entry = tkinter.Entry(self.choose_ip_and_port_root)

		ip_label.grid(row=1, column=0)
		ip_entry.grid(row=1, column=1)
		port_label.grid(row=2, column=0)
		port_entry.grid(row=2, column=1)

		connect_button = tkinter.Button(self.choose_ip_and_port_root, text='Connect', command=self.start_gui_main)
		connect_button.grid(row=3, column=0, columnspan=2)

		self.choose_ip_and_port_root.mainloop()

	def start_gui_main(self):
		new_gui = ClientGui()
		time.sleep(1)
		new_gui.start()

test = Login()
test.start()