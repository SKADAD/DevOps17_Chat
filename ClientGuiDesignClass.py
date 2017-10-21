import tkinter

class ClientGui:

	def __init__(self, servers_ip_, servers_port_):
		self.servers_ip = servers_ip_
		self.servers_port = servers_port_

		self.root = tkinter.Tk()
		# Settings for self.root
		self.root.columnconfigure(0, weight=4, minsize=200)
		self.root.columnconfigure(2, weight=2, minsize=200)
		self.root.rowconfigure(0, weight=1, minsize=200)
		self.root.rowconfigure(1, weight=4, minsize=200)
		self.root.rowconfigure(2, weight=2, minsize=200)

		# base frames for GUI
		self.top_left_frame = tkinter.Frame(self.root, bg='red')
		self.top_right_frame = tkinter.Frame(self.root, bg='blue', width=100, height = 50)
		self.center_left_frame = tkinter.Frame(self.root, bg='green', width=200, height = 100)
		self.center_right_frame = tkinter.Frame(self.root, bg='yellow', width=100, height = 100)
		self.bottom_frame = tkinter.Frame(self.root, bg='white', width=300, height = 50)

		# variables for easy change of design
		self.font = 'Calibri',
		self.fontsize = '14'
		self.fontsize_header = '20'
		self.backgroundcolor = 'white'
		self.framecolor = 'green'

	def start(self):
		self.create_base_frames()
		self.top_left_frame_create()
		self.top_right_frame_create()
		self.root.mainloop()


	def create_base_frames(self):

		self.top_left_frame.grid(row=0, column=0, columnspan=2)
		self.top_right_frame.grid(row=0, column=2)
		self.center_left_frame.grid(row=1, column=0, columnspan=2)
		self.center_right_frame.grid(row=1, column=2)
		self.bottom_frame.grid(row=2, column=0, columnspan=3)

	def top_left_frame_create(self):
		program_name_label = tkinter.Label(self.top_left_frame, text='GONE CHATT', font=(self.font, self.fontsize))
		program_name_label.grid(row=0, column=0)

	def top_right_frame_create(self):
		user_info_frame = tkinter.Frame(self.top_right_frame, bg = 'white', width= 20, height = 20, pady=10, highlightbackground='blue',highlightthickness=2)
		user_info_frame.grid(row=0, column=0)





test = ClientGui(16, 16)
test.start()