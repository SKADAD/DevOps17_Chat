import tkinter

from Client.View import ClientGuiFunctions


class ClientGui:

	def __init__(self):
		self.servers_ip = None
		self.servers_port = None
		self.user_name = '1'
		self.user_ip = '1'
		self.user_port = '1'

		self.root = tkinter.Tk()
		self.create_ip_port_frame()
		self.root.title('GONE CHAT')
		self.root.iconbitmap(default='../../images/ikon.ico')
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
		self.top_left_frame = tkinter.Frame(self.root, bg='white')
		self.top_right_frame = tkinter.Frame(self.root)
		self.center_left_frame = tkinter.Frame(self.root, bg='white', relief='ridge', borderwidth=2)
		self.center_right_frame = tkinter.Frame(self.root, bg='white', relief='ridge', borderwidth=2)
		self.bottom_frame = tkinter.Frame(self.root, bg='white')

		# variables for easy change of design
		self.font = 'calibri',
		self.font_size = '14'
		self.font_size_header = '20'
		self.background_color = 'white'
		self.frame_color = 'green'

		# Text widgets created
		self.chat_window = tkinter.Text(self.center_left_frame, wrap=tkinter.WORD, font=(self.font, 12))
		self.send_message_frame = tkinter.Frame(self.bottom_frame)
		self.input_window = tkinter.Text(self.send_message_frame, width=50, height=3, borderwidth=2, wrap=tkinter.WORD, relief='ridge', font=(self.font, 12))



		self.list_of_active_users = ['Kim', 'Nabil','Peter']

	def start(self):
		self.create_base_frames()
		self.top_left_frame_create()
		self.top_right_frame_create()
		self.center_left_frame_create()
		self.center_right_frame_create()
		self.bottom_frame_create()
		self.root.mainloop()

	def create_ip_port_frame(self):
		def sub_func_set_ip_and_port():
			self.servers_ip = ip_entry.get()
			self.servers_port = int(port_entry.get())

			connect_button.configure(state='disabled')
			choose_ip_and_port_root.withdraw()
			choose_ip_and_port_root.quit()

			return True



		choose_ip_and_port_root = tkinter.Toplevel()
		choose_ip_and_port_root.transient(self.root)

		top_label = tkinter.Label(choose_ip_and_port_root, text='Enter IP and Port of Server')
		top_label.grid(row=0, column=0, columnspan=2)

		ip_label = tkinter.Label(choose_ip_and_port_root, text='IP: ')
		ip_entry = tkinter.Entry(choose_ip_and_port_root)

		port_label = tkinter.Label(choose_ip_and_port_root, text='Port: ')
		port_entry = tkinter.Entry(choose_ip_and_port_root)

		ip_label.grid(row=1, column=0)
		ip_entry.grid(row=1, column=1)
		port_label.grid(row=2, column=0)
		port_entry.grid(row=2, column=1)

		connect_button = tkinter.Button(choose_ip_and_port_root, text='Connect', command=sub_func_set_ip_and_port)
		connect_button.grid(row=3, column=0, columnspan=2)

		choose_ip_and_port_root.mainloop()


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
		logo_image = tkinter.PhotoImage(file='../../images/Gone_logo.png')
		logo_label = tkinter.Label(self.top_left_frame, image=logo_image, border=0, bg='white')
		logo_label.image = logo_image
		logo_label.grid(row=0, column=0, pady=15, sticky='w')

	def top_right_frame_create(self):
		user_info_frame = tkinter.Frame(self.top_right_frame, bg = '#3d85c6', width= 20, height = 20, pady=10, relief="sunken", borderwidth=1)
		user_info_frame.grid(row=0, column=0, ipadx=10)

		user_label = tkinter.Label(user_info_frame, text='Username: ', justify='left', bg = '#3d85c6', fg='white', font=(self.font, 12))
		username_label = tkinter.Label(user_info_frame, text=self.user_name, bg = '#3d85c6', fg='white', font=(self.font, 12))
		ip_label = tkinter.Label(user_info_frame, text='User IP: ', justify='left', bg = '#3d85c6', fg='white', font=(self.font, 12))
		user_ip_label = tkinter.Label(user_info_frame, text=self.user_ip, bg = '#3d85c6', fg='white', font=(self.font, 12))
		port_label = tkinter.Label(user_info_frame, text='User Port: ', justify='left', bg = '#3d85c6', fg='white', font=(self.font, 12))
		user_port_label = tkinter.Label(user_info_frame, text=self.user_port, anchor='w', bg = '#3d85c6', fg='white', font=(self.font, 12))

		user_label.grid(row=0, column=0, sticky='w', padx=10)
		username_label.grid(row=0, column=1, sticky='w')

		ip_label.grid(row=1, column=0, sticky='w', padx=10)
		user_ip_label.grid(row=1, column=1, sticky='w')

		port_label.grid(row=2, column=0, sticky='w', padx=10)
		user_port_label.grid(row=2, column=1, sticky='w')

		properties_image = tkinter.PhotoImage(file='../../images/button_properties.png')
		change_userinfo_button = tkinter.Button(user_info_frame, image=properties_image, borderwidth=0, background='#3d85c6', activebackground='#3d85c6')
		change_userinfo_button.image = properties_image
		change_userinfo_button.grid(row=3, column=0, pady=(10, 0), padx=10)

		log_out_image=tkinter.PhotoImage(file='../../images/button_log-out.png')
		log_out_button = tkinter.Button(user_info_frame, image=log_out_image, borderwidth=0, background='#3d85c6', activebackground='#3d85c6')
		log_out_button.image = log_out_image
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

	def center_right_frame_create(self):
		def send_private_message(event):
			chosen_user = self.list_of_active_users[active_user_list.curselection()[0]]
			self.input_window.delete('1.0', 'end')
			self.input_window.insert('1.0', '@{} '.format(chosen_user))

		active_user_list = tkinter.Listbox(self.center_right_frame, font=(self.font, 12))
		active_user_list.grid(row=0, column=0, sticky='nswe')

		active_user_list.bind('<Button-3>', send_private_message)

		for user in self.list_of_active_users:
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
			message = self.input_window.get("1.0", 'end-1c')
			if message.isspace() or len(message) == 0:
				self.input_window.delete('1.0', 'end')
			else:
				#ClientGuiFunctions.send_message()
				ClientGuiFunctions.print_message_in_text_frame(message, self.chat_window)
				self.input_window.delete('1.0', 'end')

		def get_message_from_input_window_with_enter(event):
			get_message_from_input_window()
			return 'break'

		def new_line(event):
			self.input_window.insert('insert', '{}'.format(''))

		self.send_message_frame.grid(row=0, column=0)
		self.input_window.bind('<Return>', get_message_from_input_window_with_enter)
		self.input_window.bind('<Shift-Return>', new_line)

		self.input_window.grid(row=0, column=0, sticky='nswe')

		'''
		Scrollbar for send_widget. Saved for possible later implemention. If not implemented before release, delete this
		message_send_scrollbar = tkinter.Scrollbar(input_window)
		message_send_scrollbar.pack(side='right', fill='y')

		input_window.configure(yscrollcommand=message_send_scrollbar.set)
		message_send_scrollbar.config(command=input_window.yview)
		'''
		send_image = tkinter.PhotoImage(file='../../images/button_send.png')
		send_button = tkinter.Button(self.bottom_frame, image=send_image, command=get_message_from_input_window, borderwidth=0)
		send_button.image = send_image
		send_button.grid(row=1, column=0, sticky='e', padx=10, pady=10)

# TODO - Dropdown for activeclientlist

test = ClientGui()
test.start()
