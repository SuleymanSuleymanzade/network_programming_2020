import socket

HOST, PORT = 'localhost', 1234

message = 'this is my message to the server'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.sendall(bytes(message, "utf-8"))

server_msg = str(sock.recv(2048),'utf-8')
print(f'{server_msg}')
sock.close()