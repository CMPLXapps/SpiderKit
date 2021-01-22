import socket, os, json, time
with open('cfg/settings.json', 'r') as file:
	settings = json.load(file)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), settings['kill-port']))
s.listen()
bd, addr = s.accept()
bd.send(b'k_str')
time.sleep(1)