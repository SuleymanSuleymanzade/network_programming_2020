import smtplib 
import os
from email.message import EmailMessage
import time
class MetaSingleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super().__call__(*args, **kwargs)
		return cls._instances[cls]


class EmailSMTPServer:

	def __init__(self, from_email, from_pass, server = 'smtp.gmail.com', port = 587):
		
		self.from_email = from_email
		self.from_pass = from_pass 
		self.server = server
		self.port = port
		self.message = None

		self.smtpobj = smtplib.SMTP(self.server, self.port)
		self.smtpobj.login(self.from_email, self.from_pass)
		self.smtpobj.ehlo()
		self.smtpobj.starttls()
		self.smtpobj.ehlo()
		

	def create_message(self, subject, body):
		self.message = EmailMessage()
		self.message['Subject'] = subject
		self.message.set_content(body)
		self.message['From'] = self.from_email

	def send(self, receiver):
		self.message['To'] = receiver
		self.smtpobj.send_message(self.message)

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

	students = 'elkhan.hebibov.std@bhos.edu.az'
	password = os.environ.get('GMAIL_TEST')
	email = EmailSMTPServer('suleymanzadesuleyman@gmail.com', password)
	email.create_message("The second message", "This is an example with singleton")
	email.send(students)


if __name__ == "__main__":
	main()


