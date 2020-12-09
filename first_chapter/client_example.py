import socket 

HOST = '127.0.0.1'
PORT = 65530

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.connect((HOST, PORT))
	sock.sendall(b'Welcome to the network programming')
	d = sock.recv(2048)

print('We recieved the data ', repr(d))

