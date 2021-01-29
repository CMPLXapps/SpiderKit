import hashlib
while True:
	flag = 0
	pass_hash = input('Enter md5 hash: ')
	wordlist = input('File path: ')
	try:
		with open(wordlist, 'r') as wordlistFile:
			for i in pass_file:
				enc_wrd = bytes(i, 'utf-8')
				digest = hashlib.md5(enc_wrd.strip()).hexdigest()
				if digest == pass_hash:
					print('Password Found!')
					print(f'Password is: {word}')
					flag = 1
					break
			if flag == 0:
				print('Password not found...')
	except:
		print('No File Found...')
		continue