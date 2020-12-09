import socket 
HEADERSIZE = 16

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
	msg = ""
	new_msg = True 

	while True:
		temp_msg = s.recv(32)
		if new_msg:
			msglen = int(temp_msg[:HEADERSIZE])
			new_msg = False

		print(f"the length is {msglen}")
		
		msg += temp_msg.decode("utf-8")
		if len(msg) - HEADERSIZE == msglen:
			print(msg[HEADERSIZE:])
			new_msg = True
s.close()








