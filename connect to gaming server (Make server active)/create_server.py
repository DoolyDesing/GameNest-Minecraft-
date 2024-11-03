import requests, random, json

# token = 'a7bb7d93acf6fcea1a9e387059b505b8a71f5d73c6236861fdca59796eed4411f3d9d8c1156cacb40d18063918652f29'
# my_ssh = '4b:9d:36:18:f7:cf:f8:7b:61:8a:8e:48:d3:74:52:17'

def create_server(token, my_ssh):
	url = 'https://api.cloudvps.reg.ru/v1/reglets'
	headers = {
	    'Authorization': f'Bearer {token}',
	    'Content-Type': 'application/json'
	}
	#Name generete
	game = 'minecraft'
	id = ''
	id_len = 5
	for x in range(id_len):
		id += str(random.randrange(0, 10, 1))
	name = game + id
	image = '1662177' #ubuntu-22.04 LTS
	slug = 'base-1'
	params = {
	    "name": name,
	    "size": slug,
	    "image": image,
	    "ssh_keys": [my_ssh],
	    "backups": False
	}
	res = requests.post(url, headers = headers, data = json.dumps(params))
	if res.status_code == 201:
		print("Сервер создан")
		return(res.json())
	else:
		print(f"Ошибка при создании сервера. Статус {res.status_code}, сообщение: {res.text}")