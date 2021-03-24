import json, random
with open('cfg/charDict.json', 'r') as file:
	charDict = json.load(file)
with open('cfg/settings.json', 'r') as file:
	settings = json.load(file)
token = ''
for i in range(40):
	rand = random.randint(0, 61)
	char = list(charDict.keys())[list(charDict.values()).index(rand)]
	token += char
settings['token'] = token
del token
with open('cfg/settings.json', 'w') as file:
	json.dump(settings, file, indent=4)