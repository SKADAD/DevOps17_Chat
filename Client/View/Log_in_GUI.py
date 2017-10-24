import tkinter
import time
import tkinter.messagebox

from Client.View.ClientGuiDesignClass import ClientGui

class Login:

	def __init__(self):
		self.choose_ip_and_port_root = tkinter.Tk()
		self.ip = None
		self.port = None
		self.choose_ip_and_port_root.configure(bg='white')

	def start(self):
		def sub_func_set_ip_and_port():

			ip_entered = ip_entry.get()
			port_entered = port_entry.get()

			if (len(ip_entered) == 0 or len(port_entered) == 0) or (ip_entered.isspace() or port_entered.isspace()):
				tkinter.messagebox.showwarning(title='Error', message='Cant leave fields empty.')
				return
			try:
				self.servers_port = int(port_entered)
				self.servers_ip = ip_entered
			except ValueError:
				tkinter.messagebox.showwarning(title='Error', message='Port can only contain numbers')
				return

			self.start_gui_main()


		top_label = tkinter.Label(self.choose_ip_and_port_root, text='Enter IP and Port of Server', bg='white', font=('calibri', 10))
		top_label.grid(row=0, column=0, columnspan=2)

		ip_label = tkinter.Label(self.choose_ip_and_port_root, text='IP: ', bg='white', font=('calibri', 10))
		ip_entry = tkinter.Entry(self.choose_ip_and_port_root, bg='lightgray')

		port_label = tkinter.Label(self.choose_ip_and_port_root, text='Port: ',bg='white', font=('calibri', 10))
		port_entry = tkinter.Entry(self.choose_ip_and_port_root, bg='lightgray')

		ip_label.grid(row=1, column=0)
		ip_entry.grid(row=1, column=1)
		port_label.grid(row=2, column=0)
		port_entry.grid(row=2, column=1)

		connect_button = tkinter.Button(self.choose_ip_and_port_root, text='Connect', command=sub_func_set_ip_and_port)
		connect_button.grid(row=3, column=0, columnspan=2)

		self.choose_ip_and_port_root.mainloop()

	def start_gui_main(self):
		self.choose_ip_and_port_root.destroy()
		new_gui = ClientGui(self.ip, self.port)
		new_gui.start()
