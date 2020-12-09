import paramiko 
import os
import datetime 
username, passw, ip = ('sysadmin','123', '192.168.0.199')
#passw = os.environ['ssh_thinkpad_password']

hosts = {
	'host1':{
		'ip': '192.168.0.199',
		'pass': '123'
		'username': 'sysadmin'
	}
}

def make_routine_work(host_lists):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	hostname, username, passwd =  '', '', ''
	for host in hosts:
		hostname = host['ip']
		username = host['username']
		passw = host['pass']
		client.connect(hostname = ip, username=username, password=passw)
		command = "sudo apt-get update && upgrade && dist-upgrade;"
		stdin, stdout, stderr = client.exec_command(command)
		stdout = stdout.readlines()
		for line in stdout:
			print(line)


now = datetime.time.now()
if (now.hour == 12):
	make_routine_work(hosts)
