import socket 
import threading 

# [message length][message data]
#  ....32 data

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname(socket.gethostname()), 1234))

def handle():
	pass

def service(conn, addr, show_status = True):
	print(f"server connected {addr}")
	while True:
		message_length = conn.recv(32).decode('UTF-8')
		if not message_length:
			break
		message_length = int(message_length)
		message_data =  conn.recv(message_length).decode('UTF-8')

		if message_data == 'STOP_SESSION':
			break 

		if show_status:
			print(f"from {addr}: {message_data}")
		conn.send('The message has been recieved'.encode('UTF-8'))
	conn.close()


def server_process():
	server.listen()
	print("server is started")
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=service, args = (conn, addr))
		thread.start()
		print(f'thread number is {threading.activeCount() - 1}')

server_process()	













