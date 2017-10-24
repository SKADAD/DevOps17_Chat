import tkinter
import tkinter.messagebox

from Client.View import ClientGuiFunctions


class ClientGui:

	def __init__(self, ip, port):
		self.servers_ip = ip
		self.servers_port = port
		self.user_name = '1'
		self.user_ip = '1'
		self.user_port = '1'

		self.root = tkinter.Tk()
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
		# Start connection with server
		self.create_base_frames()
		self.top_left_frame_create()
		self.top_right_frame_create()
		self.center_left_frame_create()
		self.center_right_frame_create()
		self.bottom_frame_create()
		self.log_in_frame()
		self.root.mainloop()

	def log_in_frame(self):

		def sub_func_get_name_and_code():
			entered_login_name = log_in_name_entry.get()
			entered_code = code_entry.get()

			if (len(entered_login_name) == 0 or len(entered_code) == 0) or (entered_login_name.isspace() or entered_code.isspace()):
				tkinter.messagebox.showwarning(title='Error', message='Fields cant be empty')
			else:
				sub_func_log_in(entered_login_name, entered_code)



		def sub_func_register():
			def sub_sub_func_close_window():
				register_toplevel.grab_release()
				register_toplevel.withdraw()
				register_toplevel.quit()

			def sub_sub_func_register_new_user():
				entered_user_name = user_name_entry.get()
				entered_user_nickname = nickname_entry.get()
				entered_user_code = code_entry.get()
				if (len(entered_user_name) == 0 or len(entered_user_nickname) == 0 or len(entered_user_code) == 0) or (entered_user_name.isspace() or entered_user_nickname.isspace() or entered_user_nickname.isspace()):
					tkinter.messagebox.showwarning(title='Error', message='Fields cant be empty')
				else:
					result = ClientGuiFunctions.register_client_to_server(entered_user_name, entered_user_nickname, entered_user_code)
					if result:
						sub_func_log_in(entered_user_name, entered_user_code)

					elif result == -1:
						tkinter.messagebox.showwarning(title='Error', message='Account with username {} already exists'.format(entered_user_name))

					elif result == -2:
						tkinter.messagebox.showwarning(title='Error', message='That nickname is already taken')


			register_toplevel = tkinter.Toplevel(log_in_toplevel)
			register_toplevel.configure(bg='white')
			register_toplevel.transient(log_in_toplevel)
			register_toplevel.attributes('-topmost', 'true')
			register_toplevel.grab_set()


			top_label = tkinter.Label(register_toplevel, text='Enter IP and Port of Server', bg='white',
									  font=('calibri', 10))
			top_label.grid(row=0, column=0, columnspan=2)

			user_name_label = tkinter.Label(register_toplevel, text='User name: ', bg='white', font=('calibri', 10))
			user_name_entry = tkinter.Entry(register_toplevel, bg='lightgray')

			nickname_label = tkinter.Label(register_toplevel, text='Nickname: ', bg='white', font=('calibri', 10))
			nickname_entry = tkinter.Entry(register_toplevel, bg='lightgray')

			code_label = tkinter.Label(register_toplevel, text='Code: ', bg='white', font=('calibri', 10))
			code_entry = tkinter.Entry(register_toplevel, bg='lightgray')

			user_name_label.grid(row=1, column=0)
			user_name_entry.grid(row=1, column=1)
			nickname_label.grid(row=2, column=0)
			nickname_entry.grid(row=2, column=1)
			code_label.grid(row=3, column=0)
			code_entry.grid(row=3, column=1)

			button_bottom_frame = tkinter.Frame(register_toplevel)
			button_bottom_frame.grid(row=4, column=0, columnspan=2)

			register_button = tkinter.Button(button_bottom_frame, text='Register', command=sub_sub_func_register_new_user)
			register_button.grid(row=0, column=0, padx=10)
			cancel_button = tkinter.Button(button_bottom_frame, text='Cancel', command=sub_sub_func_close_window)
			cancel_button.grid(row=0, column=1)

			register_toplevel.mainloop()

		def sub_func_close_window():
			close_program = tkinter.messagebox.askyesno(title='Close program', message='Closing this windows closes the program.\nDo you want to continue')
			if close_program == True:
				# close connection
				self.root.destroy()

		def sub_func_log_in(login_name, code):

			# Check log in towards server

			log_in_toplevel.grab_release()
			log_in_toplevel.withdraw()
			log_in_toplevel.quit()

		log_in_toplevel = tkinter.Toplevel(self.root)
		log_in_toplevel.transient(self.root)
		log_in_toplevel.attributes('-topmost', 'true')
		log_in_toplevel.grab_set()
		log_in_toplevel.protocol('WM_DELETE_WINDOW', sub_func_close_window)

		top_label = tkinter.Label(log_in_toplevel, text='Log in or register')
		top_label.grid(row=0, column=0, columnspan=2)

		log_in_name_label = tkinter.Label(log_in_toplevel, text='IP: ')
		log_in_name_entry = tkinter.Entry(log_in_toplevel)

		code_label = tkinter.Label(log_in_toplevel, text='Port: ')
		code_entry = tkinter.Entry(log_in_toplevel)

		log_in_name_label.grid(row=1, column=0)
		log_in_name_entry.grid(row=1, column=1)
		code_label.grid(row=2, column=0)
		code_entry.grid(row=2, column=1)

		button_bottom_frame= tkinter.Frame(log_in_toplevel)
		button_bottom_frame.grid(row=3, column=0, columnspan=2)

		connect_button = tkinter.Button(button_bottom_frame, text='Log in', command=sub_func_get_name_and_code)
		connect_button.grid(row=0, column=0, padx=10)
		register_button = tkinter.Button(button_bottom_frame, text='Register', command=sub_func_register)
		register_button.grid(row=0, column=1)

		log_in_toplevel.mainloop()


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

test = ClientGui('127.0.0.1', 9999)
test.start()
