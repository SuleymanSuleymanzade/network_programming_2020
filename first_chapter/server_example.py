import socket 

HOST = '127.0.0.1'
PORT = 65530

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.bind((HOST, PORT))
	sock.listen()
	conn, addr = sock.accept()
	with conn:
		print('we are connected with', addr)
		while True:
			d = conn.recv(2048)
			if not d:
				break
			conn.sendall(d)
