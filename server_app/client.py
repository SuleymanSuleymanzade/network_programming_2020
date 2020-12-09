import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostbyname(socket.gethostname()), 1234))

def send_message(message):
	data = message.encode('UTF-8')
	message_length = len(data)
	message_length_encoded = str(message_length).encode('UTF-8')
	message_length_encoded += b' ' * (32 - len(message_length_encoded))

	client.send(message_length_encoded)
	client.send(data)

	print(client.recv(4096).decode('UTF-8'))

send_message('message 1')
input()
send_message('message 2')
input()
send_message('message 3')

send_message('STOP_SESSION')


