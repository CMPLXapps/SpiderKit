import socket
import json
srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
	with open('cfg/settings.json', 'r') as file:
		settings = json.load(file)
	ip = socket.gethostname()
	port = settings['port']
	print(' - Use \'@HELP\' or \'::?\' for a list of commands.')
	print(' - Use \'@GO\' or \'::!\' to start listening for connections.')
	usrin = input('>> ')
	if usrin.replace(' ', '') == '@HELP' or usrin.replace(' ', '') == '::?':
		with open('cfg/help.txt', 'r') as file:
			print(file.read())
	srvr.bind((ip, port))
	while True:
		data = srvr.recv(1024).strip()
		msg = data.decode()
		if '@HELP' in msg or '::?' in msg:
			with open('cfg/help.txt', 'r') as file:
				print(file.read())
		elif msg.find('@HOST ') == 0: or msg.find('::h') == 0:
			pass