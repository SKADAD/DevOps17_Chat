import tkinter
import ClientGuiFunctions

class ClientGui:

	def __init__(self, servers_ip_, servers_port_, user_name_, client_ip_, client_port_):
		self.servers_ip = servers_ip_
		self.servers_port = servers_port_
		self.user_name = user_name_
		self.client_ip = client_ip_
		self.client_port = client_port_

		self.root = tkinter.Tk()
		self.root.configure(bg='white')
		self.root.minsize(width=800, height=600)


		# Settings for self.root
		self.root.columnconfigure(0, weight=2, minsize=200)
		self.root.columnconfigure(1, weight=2, minsize=500)
		self.root.columnconfigure(2, weight=2, minsize=200)
		self.root.rowconfigure(0, weight=1, minsize=200)
		self.root.rowconfigure(1, weight=5, minsize=200)
		self.root.rowconfigure(2, weight=1, minsize=200)

		# base frames for GUI
		self.top_left_frame = tkinter.Frame(self.root, bg='red', highlightbackground='blue',highlightthickness=2)
		self.top_right_frame = tkinter.Frame(self.root, bg='blue', highlightbackground='blue',highlightthickness=2)
		self.center_left_frame = tkinter.Frame(self.root, bg='green', highlightbackground='blue',highlightthickness=2)
		self.center_right_frame = tkinter.Frame(self.root, bg='yellow', width=100, height = 100, highlightbackground='blue',highlightthickness=2)
		self.bottom_frame = tkinter.Frame(self.root, bg='white', highlightbackground='blue',highlightthickness=2)

		self.chat_window = tkinter.Text(self.center_left_frame, highlightbackground='blue',highlightthickness=2)

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
		self.center_left_frame_create()
		self.center_right_frame_create()
		self.bottom_frame_create()
		self.root.mainloop()


	def create_base_frames(self):

		self.top_left_frame.grid(row=0, column=0, columnspan=2, sticky='w', padx=10)
		self.top_right_frame.grid(row=0, column=2)
		self.center_left_frame.grid(row=1, column=0, columnspan=2, sticky='nswe', padx=10)
		self.center_right_frame.grid(row=1, column=2)
		self.bottom_frame.grid(row=2, column=0, columnspan=2, sticky='e', padx=10)

		#self.center_left_frame.rowconfigure(0, weight=2)
		#self.center_left_frame.columnconfigure(0, weight=2)

	def top_left_frame_create(self):
		logo_image = tkinter.PhotoImage(file='G.ONE.png')
		logo_label = tkinter.Label(self.top_left_frame, image=logo_image, border=0)
		logo_label.image = logo_image
		logo_label.grid(row=0, column=0, pady=15, sticky='w')

	def top_right_frame_create(self):
		user_info_frame = tkinter.Frame(self.top_right_frame, bg = 'white', width= 20, height = 20, pady=10, highlightbackground='blue',highlightthickness=2)
		user_info_frame.grid(row=0, column=0)

		user_label = tkinter.Label(user_info_frame, text='Username: ')
		username_label = tkinter.Label(user_info_frame, text=self.user_name)

		ip_label = tkinter.Label(user_info_frame, text='User IP: ')
		user_ip_label = tkinter.Label(user_info_frame, text=self.client_ip)

		port_label = tkinter.Label(user_info_frame, text='User Port: ')
		user_port_label = tkinter.Label(user_info_frame, text=self.client_port)


		user_label.grid(row=0, column=0, sticky='w')
		username_label.grid(row=0, column=1)

		ip_label.grid(row=1, column=0, sticky='w')
		user_ip_label.grid(row=1, column=1)

		port_label.grid(row=2, column=0, sticky='w')
		user_port_label.grid(row=2, column=1)

		change_userinfo_button = tkinter.Button(user_info_frame, text='Properties')
		change_userinfo_button.grid(row=3, column=0)

		log_out_button = tkinter.Button(user_info_frame, text='Log out')
		log_out_button.grid(row=3, column=1)

	def center_left_frame_create(self):
		self.chat_window.grid(row=0, column=0, columnspan=2, sticky='nswe')
		self.chat_window.configure(state="disabled")


	def center_right_frame_create(self):
		pass

	def bottom_frame_create(self):
		def sub_func_get_input():
			message = str(input_user.get())
			if len(message) == 0:
				pass
			else:
				ClientGuiFunctions.print_message_in_text_frame(message, self.chat_window)

		input_user = tkinter.StringVar()
		input_field = tkinter.Entry(self.bottom_frame, text=input_user, width=30, highlightbackground='gray',highlightthickness=1)
		input_field.grid(row=1, column=0)
		send_button = tkinter.Button(self.bottom_frame, text='Send',
									 command=lambda: (sub_func_get_input(),input_field.delete(0, 'end') ))
		send_button.grid(row=3, column=0, pady=10, padx=10, sticky='e')





test = ClientGui('16', '16', 'Kim', '127.0.0.1', '5555')
test.start()