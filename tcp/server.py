import socket 
HEADERSIZE = 16

msg = "this msg from the server"



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(1)

while True:
	client_sock, addr = s.accept()
	print(f"connected with {addr}")

	send_msg = f"{len(msg):<{HEADERSIZE}}" + msg
	client_sock.send(send_msg.encode("UTF-8"))

s.close()