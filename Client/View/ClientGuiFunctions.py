import time
from Client.Controller.ClientBackendMain import ClientBackend
from Client.Controller.ClientSendClass import Sender

def print_message_in_text_frame(message, chat_window):
	# Enable insert to chat_window
	chat_window.configure(state="normal")
	# Inserts message at beginning of chat
	chat_window.insert('insert', '{}\n'.format(message))
	chat_window.see('end')
	# Disables insert to chat_window
	chat_window.configure(state="disabled")

def listofusersupdate(list_of_active_users,active_user_list):
    for user in list_of_active_users:
        active_user_list.insert('end', user)

def register_client_to_server(socket, name, nickname, code):
	message_to_server = '2 '+name+' '+code+' '+nickname
	socket.client.send(str.encode(message_to_server))
	result = socket.client.recv(1024).decode()
	time.sleep(0.5)
	if result == 'account created':
		socket.start_reciever()
		return 0
	elif result == 'account exists':
		return -1
	elif result == 'nickname exists':
		return -2

def log_in_client(socket, name, code):
	message_to_server = '1'+name+' '+code
	socket.client.send(str.encode(message_to_server))
	result = socket.client.recv(1024).decode()
	time.sleep(0.5)
	if result == 'correct':
		socket.start_reciever()
		return 0
	elif result == 'wrong password':
		return -1
	elif result == 'no account':
		return -2

def print_message_in_text_frame_right(message, chat_window):
	# Enable insert to chat_window
	chat_window.configure(state="normal")
	# Inserts message at beginning of chat
	chat_window.tag_configure('tag-right', justify='right')
	chat_window.insert('end', '{}\n'.format(message),'tag-right')
	# Disables insert to chat_window
	chat_window.configure(state="disabled")