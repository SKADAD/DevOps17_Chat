

def print_message_in_text_frame(message, chat_window):
	chat_window.configure(state="normal")
	chat_window.insert('insert', '{}\n'.format(message))
	chat_window.configure(state="disabled")

