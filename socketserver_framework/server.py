import socketserver
class TCPServerHandler( socketserver.BaseRequestHandler):

	def handle(self):
		self.message = self.request.recv(2048)
		print(f"{self.client_address[0]} sent message:")
		print(self.message)
		self.request.sendall(f'ok we saw your message: {self.message}', 'utf-8'))

def main():
	HOST, PORT = 'localhost', 1234

	with socketserver.TCPServer((HOST, PORT), TCPServerHandler) as server:
		print('Server has started ...')
		server.serve_forever()


if __name__ == "__main__":
	main()