# from Client.Controller.ClientBackendMain import Clientbackend

def print_message_in_text_frame(message, chat_window):
	# Enable insert to chat_window
	chat_window.configure(state="normal")
	# Inserts message at beginning of chat
	chat_window.insert('insert', '{}\n'.format(message))
	chat_window.see('end')
	# Disables insert to chat_window
	chat_window.configure(state="disabled")



def send_message(message):
	pass

def register_client_to_server(name, nickname, code):
	# register client
	# return True
	pass

def print_message_in_text_frame_right(message, chat_window):
	# Enable insert to chat_window
	chat_window.configure(state="normal")
	# Inserts message at beginning of chat
	chat_window.tag_configure('tag-right', justify='right')
	chat_window.insert('end', '{}\n'.format(message),'tag-right')
	# Disables insert to chat_window
	chat_window.configure(state="disabled")