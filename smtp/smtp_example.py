import smtplib 
import os
from email.message import EmailMessage
import time
import imghdr

class MetaSingleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super().__call__(*args, **kwargs)
		return cls._instances[cls]


class EmailSMTPServer:

	def __init__(self, from_email, from_pass, server = 'smtp.gmail.com', port = 465):
		
		self.from_email = from_email
		self.from_pass = from_pass 
		self.server = server
		self.port = port
		self.message = None

	def create_message(self, subject, body, attachement = None):
		m = EmailMessage()
		m['Subject'] = subject
		m.set_content(body)
		m['From'] = self.from_email
		
		if attachement:
			file = open(attachement, 'rb')
			m.add_attachment(file.read(), 
				maintype='image',
				subtype = imghdr.what(file.name),
				filename=file.name
			)
			file.close()

		self.message = m


	def send(self, receiver):	
		with smtplib.SMTP_SSL(self.server, self.port) as smtpobj:

			smtpobj.login(self.from_email, self.from_pass)
			
			if isinstance(receiver, str):
				self.message['To'] = receiver

			if isinstance(receiver, list):
				self.message['To'] = ', '.join(receiver)

			smtpobj.send_message(self.message)
					#print('ok')
class Wrapper:
	def __init__(self):
		pass

	def add_server(self, server):
		self.servers.append(server)

	def activate_server(self, name):
		for server in self.servers:
			if server.name == name:
				server.activate

def main():

	students = 'suleyman.suleymanzade@bhos.edu.az'
	password = os.environ.get('GMAIL_TEST')
	email = EmailSMTPServer('suleymanzadesuleyman@gmail.com', password)
	email.create_message("The second message", "This is an example with singleton", attachement = "./download.jpeg")

	email.send(students)

if __name__ == "__main__":
	main()
