class psftp:
	def send(sobj, comm, path, target='.'):
		pass
	def process(string):
		if msg.find('-t') == 0 or msg.find('--target') == 0:
			msg = msg.replace('-t ', '')
			msg = msg.replace('--target ', '')
			if msg[0] == '\'' or msg[0] == '"':
				temp = msg[0]
				msg[1:]
			else:
				print('Err; You need to specify a destination path when using -t and --target')
				client.send(b'@RESEND')
				continue
			datalist = {'target': msg['']}