
def print_message_in_text_frame(message, chat_window):
	# Enable insert to chat_window
	chat_window.configure(state="normal")
	# Inserts message at beginning of chat
	chat_window.insert('1.0', '{}\n'.format(message))
	# Disables insert to chat_window
	chat_window.configure(state="disabled")

def send_message(message):
