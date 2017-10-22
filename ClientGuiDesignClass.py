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
		self.top_right_frame = tkinter.Frame(self.root)
		self.center_left_frame = tkinter.Frame(self.root, bg='green', highlightbackground='blue',highlightthickness=2)
		self.center_right_frame = tkinter.Frame(self.root, bg='yellow', highlightbackground='blue',highlightthickness=2)
		self.bottom_frame = tkinter.Frame(self.root, bg='white', highlightbackground='blue',highlightthickness=2)

		self.chat_window = tkinter.Text(self.center_left_frame, highlightbackground='blue',highlightthickness=2)

		# variables for easy change of design
		self.font = 'calibri',
		self.font_size = '14'
		self.font_size_header = '20'
		self.background_color = 'white'
		self.frame_color = 'green'

		self.list_of_active_users = ['Kim', 'Nabil','Peter']

	def start(self):
		self.create_base_frames()
		self.top_left_frame_create()
		self.top_right_frame_create()
		self.center_left_frame_create()
		self.center_right_frame_create(self.list_of_active_users)
		self.bottom_frame_create()
		self.root.mainloop()


	def create_base_frames(self):

		self.top_left_frame.grid(row=0, column=0, columnspan=2, sticky='w', padx=10)
		self.top_right_frame.grid(row=0, column=2)
		self.center_left_frame.grid(row=1, column=0, columnspan=2, sticky='nswe', padx=10)
		self.center_right_frame.grid(row=1, column=2, sticky='n')
		self.bottom_frame.grid(row=2, column=0, columnspan=2, sticky='e', padx=10)

		self.center_left_frame.rowconfigure(0, weight=3)
		self.center_left_frame.columnconfigure(0, weight=3)
		self.bottom_frame.rowconfigure(0, weight=1)
		self.bottom_frame.columnconfigure(0, weight=1)


	def top_left_frame_create(self):
		logo_image = tkinter.PhotoImage(file='G.ONE.png')
		logo_label = tkinter.Label(self.top_left_frame, image=logo_image, border=0)
		logo_label.image = logo_image
		logo_label.grid(row=0, column=0, pady=15, sticky='w')

	def top_right_frame_create(self):
		user_info_frame = tkinter.Frame(self.top_right_frame, bg = 'darkblue', width= 20, height = 20, pady=10, highlightbackground='white',highlightthickness=1)
		user_info_frame.grid(row=0, column=0, ipadx=10)

		user_label = tkinter.Label(user_info_frame, text='Username: ', justify='left')
		username_label = tkinter.Label(user_info_frame, text=self.user_name)
		ip_label = tkinter.Label(user_info_frame, text='User IP: ', justify='left')
		user_ip_label = tkinter.Label(user_info_frame, text=self.client_ip)
		port_label = tkinter.Label(user_info_frame, text='User Port: ', justify='left')
		user_port_label = tkinter.Label(user_info_frame, text=self.client_port, anchor='w')

		user_label.grid(row=0, column=0, sticky='w', padx=10)
		username_label.grid(row=0, column=1, sticky='w')

		ip_label.grid(row=1, column=0, sticky='w', padx=10)
		user_ip_label.grid(row=1, column=1, sticky='w')

		port_label.grid(row=2, column=0, sticky='w', padx=10)
		user_port_label.grid(row=2, column=1, sticky='w')

		change_userinfo_button = tkinter.Button(user_info_frame, text='Properties')
		change_userinfo_button.grid(row=3, column=0, pady=(10, 0))
		log_out_button = tkinter.Button(user_info_frame, text='Log out')
		log_out_button.grid(row=3, column=1, pady=(10, 0))

	def center_left_frame_create(self):
		self.chat_window.grid(row=0, column=0, columnspan=2, sticky='nswe')
		self.chat_window.see('end')
		self.chat_window.configure(state="disabled")

		'''
		Scrollbar for view_widget. Saved for possible later implementation. If not implemented before release, delete this
		
		chat_window_scrollbar = tkinter.Scrollbar(self.chat_window)
		chat_window_scrollbar.pack(side='right', fill='y')
		
		chat_window_scrollbar.config(command=self.chat_window.yview)
		'''

	def center_right_frame_create(self, list_of_active_users):

		active_user_list = tkinter.Listbox(self.center_right_frame)
		active_user_list.grid(row=0, column=0, sticky='nswe')


		for user in list_of_active_users:
			active_user_list.insert('end', user)




	def bottom_frame_create(self):

		'''
			Functions and input_field for send_widget. Saved for possible change of input method. If not implemented before release, delete this

		def sub_func_get_input():
			message = str(input_user.get())
			if len(message) == 0:
				pass
			else:
				ClientGuiFunctions.print_message_in_text_frame(message, self.chat_window)
				#input_field.delete(0, 'end')

		def sub_func_bind_enter(event):
			message = str(input_user.get())
			if len(message) == 0:
				pass
			else:
				ClientGuiFunctions.print_message_in_text_frame(message, self.chat_window)
				#input_field.delete(0, 'end')


		input_user = tkinter.StringVar()
		input_field = tkinter.Entry(self.bottom_frame, text=input_user, highlightbackground='gray',highlightthickness=1)
		input_field.bind("<Return>", sub_func_bind_enter)
		input_field.grid(row=1, column=0, sticky='ew')
		'''

		def get_message_from_input_window():
				message = input_window.get("1.0", 'end-1c')
				ClientGuiFunctions.print_message_in_text_frame(message, self.chat_window)

		send_message_frame=tkinter.Frame(self.bottom_frame, highlightbackground='blue', highlightthickness=2)
		send_message_frame.grid(row=0, column=0)

		input_window = tkinter.Text(send_message_frame, highlightbackground='blue', highlightthickness=2,  width=50, height=3)
		input_window.grid(row=0, column=0, sticky='nswe')

		'''
		Scrollbar for send_widget. Saved for possible later implemention. If not implemented before release, delete this
		message_send_scrollbar = tkinter.Scrollbar(input_window)
		message_send_scrollbar.pack(side='right', fill='y')

		input_window.configure(yscrollcommand=message_send_scrollbar.set)
		message_send_scrollbar.config(command=input_window.yview)
		'''

		send_button = tkinter.Button(self.bottom_frame, text='Send', command=get_message_from_input_window)
		send_button.grid(row=1, column=0, sticky='e', padx=10, pady=10)




test = ClientGui('16', '16', 'Kim', '127.0.0.1', '5555')
test.start()